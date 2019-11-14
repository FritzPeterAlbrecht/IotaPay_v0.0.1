from iota import Iota
import os.path


# Class to handle all IOTA related topics
class IotaControl:

    # init and set startup vars
    def __init__(self, config, hjson, index):

        self.api = Iota(config.getNodeUrl(), config.getSeed())
        self.secLvl = config.getSecLvl()
        self.checksum = config.getChecksum()
        self.jspath = config.getJsonPath()
        self.json = hjson
        self.index = index

    # generate new address, check if it was spent from
    def generate_new_address(self):

        if os.path.isfile(self.jspath):
            self.index = self.json.get_last_index()
        else:
            self.index = 0

        new_add = self.api.get_new_addresses(index=self.index, count=1, security_level=self.secLvl,
                                             checksum=self.checksum)

        print('generating address with index: ', self.index)
        self.new_address = str(new_add['addresses'][0])

        self.check_spent()

    # check if address has spent before
    def check_spent(self):

        # get rid of the checksum to pass to were_addresses_spent_from
        self.address_to_check = [self.new_address[0:81]]

        sp = self.api.were_addresses_spent_from(self.address_to_check)
        self.spent = sp['states'][0]
        print('address has spent before: ', self.spent)

        self.write_to_file()

    # write to file
    def write_to_file(self):

        no = self.index
        spent = self.spent
        address = self.new_address

        if os.path.isfile(self.jspath):
            self.json.write_json(no, spent, address)
            self.index += 1
        else:
            self.json.construct_json(no, spent, address)
            self.index += 1

        if spent is True:

            self.index += 1
            self.generate_new_address()

        else:
            pass

    def get_tx_object(self, tx_hash):
        self.api.get_transaction_objects(tx_hash)
        return
