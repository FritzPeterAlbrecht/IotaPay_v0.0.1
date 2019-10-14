from iota import Iota
import Configuration
import JsonHandlerClass
import os.path


# Class to handle all IOTA related topics
class IotaCtrl:

    # init and set startup vars
    def __init__(self):
        c = Configuration.Configuration()
        hj = JsonHandlerClass.HandleJson()
        self.node_url = c.node
        self.seed = c.seed
        self.index = hj.file_index
        self.spent = False
        self.new_address = str()
        self.sec_level = c.secLvl
        self.check_sum = c.checksum

    # generate new address, check if it was spent from
    def generate_new_address(self):
        c = Configuration.Configuration()
        hj = JsonHandlerClass.HandleJson()
        print('generating address with index: ', self.index, self.new_address)
        api = Iota(c.node, c.seed)
        self.new_address = api.get_new_addresses(index=self.index, count=1, security_level=c.secLvl,
                                                 checksum=c.checksum)
        self.new_address = self.new_address['addresses'][0]

        # get rid of the checksum to pass to were_addresses_spent_from
        self.address_to_check = [self.new_address[0:81]]

        # check if this address was spent from
        self.spent = api.were_addresses_spent_from(self.address_to_check)
        self.spent = self.spent['states'][0]

        # check if file exists before writing
        if os.path.isfile('./usedAddresses.json'):
            #jh = HandleJson()
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


