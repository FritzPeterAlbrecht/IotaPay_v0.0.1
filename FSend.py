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
        while count <=self.index:
            with open(self.jspath, "r") as f:
                r = json.load(f)
                self.read_address = r["usedAddresses"]["ids"][count]["address"]
                self.address_list.append(self.read_address)
                count += 1
                if count == self.index:
                    self.check_balances()
                    break

    # check the collected address list for their balances
    def check_balances(self):
        self.result = self.api.get_balances(self.address_list)
        self.balances = self.result["balances"]
        self.sum_balances()

    # add the returned balances of all addresses
    def sum_balances(self):
        count = 0
        self.summary = 0
        for i in range(len(self.balances)):
            a = int(self.balances[count])
            self.summary = self.summary + a
            count += 1

        print('You have :', self.summary, 'iota to move.')

    def send_funds(self):
        address = str(self.owner)
        print(address)
        tx = ProposedTransaction(
            address=Address(address),
            message=TryteString.from_unicode('This tx comes from your IOTAPay Device'),
            tag=Tag('IOTAPAY'),
            value=self.summary
        )
        tx = self.api.prepare_transfer(transfers=[tx])
        result = self.api.send_trytes(tx['trytes'], depth=3, min_weight_magnitude=9)

        print('Transaction sent to the tangle!')
