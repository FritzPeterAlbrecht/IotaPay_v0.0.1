from iota import Iota
from iota import ProposedTransaction
from iota import Address
from iota import Tag
from iota import TryteString
import json


# Class to send device funds to the owners wallet
class FSend:
    def __init__(self, config, index, jspath):
        self.index = index
        self.api = Iota(config.getNodeUrl(), config.getSeed())
        self.secLvl = config.getSecLvl()
        self.checksum = config.getChecksum()
        self.jspath = jspath
        self.owner = config.getOwner()
        self.address_list = []

    # collect the used addresses from the json file
    def list_addresses(self):
        count = 0
        while count <= self.index:
            with open(self.jspath, "r") as f:
                r = json.load(f)
                self.address_list.append(r["usedAddresses"]["ids"][count]["address"])
                count += 1
                if count == self.index:
                    self.check_balances()
                    break

    # check the collected address list for their balances
    def check_balances(self):
        self.result = self.api.get_balances(self.address_list)
        self.balances = self.result["balances"]
        self.sum_balances()

    # add the balances of all addresses
    def sum_balances(self):
        count = 0
        self.summary = 0
        for i in range(len(self.balances)):
            a = int(self.balances[count])
            self.summary = self.summary + a
            count += 1

        print('You have :', self.summary, 'iota to move.')
        self.send_funds()

    # prepare tx and send funds
    def send_funds(self):
        inputs = self.address_list
        print(inputs)
        tx = ProposedTransaction(
            address=Address(self.owner),
            message=TryteString.from_unicode('IOTAPay Device V1'),
            tag=Tag('IOTAPAYTRANSACTION'),
            value=self.summary
        )
        tx = self.api.prepare_transfer(transfers=[tx], change_address=self.owner)
        result = self.api.send_trytes(tx['trytes'], depth=3, min_weight_magnitude=14)
        print('Transaction with:', self.summary, 'iota sent to the tangle!')
