from iota import Iota
from Configuration import Configuration
import JsonHandlerClass
import os.path


# Class to handle all IOTA related topics
class IotaCtrl:

    # init and set startup vars
    def __init__(self):
        c = Configuration()
        self.node = c.node
        self.seed = c.seed
        self.secLvl = c.secLvl
        self.checksum = c.checksum
        self.info = 'Welcome to IotaPay.'

    # generate new address, check if it was spent from
    def generate_new_address(self, index):

        api = Iota(self.node, self.seed)
        new_add = api.get_new_addresses(index=index, count=1, security_level=self.secLvl,
                                        checksum=self.checksum)

        print('generating address with index: ', index)
        self.new_address = str(new_add['addresses'][0])

        # get rid of the checksum to pass to were_addresses_spent_from
        self.address_to_check = [self.new_address[0:81]]

        # check if this address was spent from
        sp = api.were_addresses_spent_from(self.address_to_check)
        self.spent = sp['states'][0]
        print('address has spent before: ', self.spent)

        no = index
        spent = self.spent
        address = str(self.new_address)

        # check if file exists before writing
        if os.path.isfile('./usedAddresses.json'):
            hj = JsonHandlerClass.HandleJson()
            hj.write_json(no, spent, address)
        else:
            pass

        if spent is True:

            index = index + 1
            IotaCtrl.generate_new_address(self, index)

        else:
            pass
