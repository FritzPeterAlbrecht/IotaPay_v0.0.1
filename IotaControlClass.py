from iota import Iota
from Configuration import Configuration
from JsonHandlerClass import HandleJson
import os.path


# Class to handle all IOTA related topics
class IotaCtrl:

    # init and set startup vars
    def __init__(self):
        c = Configuration()
        hj = HandleJson()
        self.node = c.node
        self.seed = c.seed
        self.secLvl = c.secLvl
        self.checksum = c.checksum
        self.index = hj.file_index
        self.spent = False
        self.new_address = str()

    # generate new address, check if it was spent from
    def generate_new_address(self):
        print('generating address with index: ', self.index, self.new_address)
        api = Iota(self.node, self.seed)
        self.new_address = api.get_new_addresses(index=self.index, count=1, security_level=self.secLvl,
                                                 checksum=self.checksum)
        self.new_address = self.new_address['addresses'][0]

        # get rid of the checksum to pass to were_addresses_spent_from
        self.address_to_check = [self.new_address[0:81]]

        # check if this address was spent from
        self.spent = api.were_addresses_spent_from(self.address_to_check)
        self.spent = self.spent['states'][0]

        # check if file exists before writing
        if os.path.isfile('./usedAddresses.json'):
            hj = HandleJson()
            hj.write_json()
        else:
            pass

        if self.spent is True:
            self.index = self.index + 1
            self.generate_new_address()
            #jh = HandleJson()
            #jh.write_json()
        else:
            pass

        print('This is generated: ', self.index, self.spent, self.new_address)


