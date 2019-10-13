from iota import Iota
import JsonHandlerClass
import os.path


# Class to handle all IOTA related topics
class IotaCtrl:

    # init and set startup vars
    def __init__(self):
        json_handler = JsonHandlerClass.HandleJson()
        json_handler.configuration()
        self.node_url = json_handler.node_url
        self.seed = json_handler.seed
        self.index = json_handler.file_index
        self.spent = False
        self.new_address = str()
        self.sec_level = json_handler.sec_level
        self.check_sum = json_handler.check_sum

    # generate new address, check if it was spent from
    def generate_new_address(self):
        api = Iota(self.node_url, self.seed)
        self.new_address = api.get_new_addresses(index=self.index, count=1, security_level=self.sec_level,
                                                 checksum=self.check_sum)
        self.new_address = self.new_address['addresses'][0]

        # get rid of the checksum to pass to were_addresses_spent_from
        self.address_to_check = [self.new_address[0:81]]

        # check if this address was spent from
        self.spent = api.were_addresses_spent_from(self.address_to_check)
        self.spent = self.spent['states'][0]
        print(self.spent)

        # check if file exists before writing
        if os.path.isfile('./usedAddresses.json'):
            json_handler = JsonHandlerClass.HandleJson()
            json_handler.write_json()
        else:
            pass

        if self.spent is True:
            self.generate_new_address()
        else:
            pass

        print('This is generated: ', self.index, self.new_address)

        # update index for the next address
        self.index = self.index + 1
        print(self.index)
