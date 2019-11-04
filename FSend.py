from iota import Iota
from iota import ProposedTransaction
from iota import Address
from iota import Tag
from iota import TryteString


# Class to send device funds to the owners wallet
class FSend:
    def __init__(self, config, index, jspath):
        self.index = index
        self.api = Iota(config.getNodeUrl(), config.getSeed())
        self.secLvl = config.getSecLvl()
        self.checksum = config.getChecksum()
        self.jspath = jspath
        self.owner = config.getOwner()

    # search for addresses with inputs
    def get_value_addresses(self):
        response = self.api.get_inputs(start=0, stop=self.index, security_level=self.secLvl)
        self.value_addresses = response['inputs']
        self.summary = response['totalBalance']
        self.send_funds()

    # prepare tx and send funds
    def send_funds(self):
        tx = ProposedTransaction(
            address=Address(self.owner),
            message=TryteString.from_unicode('IOTAPay Device V1'),
            tag=Tag('IOTAPAYTRANSACTION'),
            value=self.summary
        )
        tx = self.api.prepare_transfer(transfers=[tx], inputs=self.value_addresses, change_address=self.owner)
        result = self.api.send_trytes(tx['trytes'], depth=3, min_weight_magnitude=14)
        print('Transaction with:', self.summary, 'iota sent to the tangle!')
