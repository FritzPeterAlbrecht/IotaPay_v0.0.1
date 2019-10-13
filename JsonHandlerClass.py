import json
import IotaControlClass


class HandleJson:
    def __init__(self):
        self.last_index = int()
        self.file_index = int()

    # load node config file
    def configuration(self):
        with open('./node_config.json', 'r') as f:
            config_file = json.load(f)
            self.node_url = config_file['Node']
            self.seed = config_file['Seed']
            self.sec_level = config_file['SecurityLevel']
            self.check_sum = config_file['CheckSum']

    # check if the json file usedAddresses is existing. If not get first address and write json file
    def construct_json(self):
        iota_ctrl = IotaControlClass.IotaCtrl()
        iota_ctrl.generate_new_address()
        self.first_address = str(iota_ctrl.new_address)
        self.spent = iota_ctrl.spent

        iota_ctrl.index = 0

        addressData = {'usedAddresses': {}}
        addressData['usedAddresses']['ids'] = []
        addressData['usedAddresses']['ids'].append({
            "id": self.file_index,
            "spent": self.spent,
            "address": self.first_address
        })
        with open('./usedAddresses.json', 'w') as f:
            json.dump(addressData, f, indent=2)

        if self.spent is True:
            print('USED! generating new address...')
            iota_ctrl.generate_new_address()
        else:
            pass

    # get last used address from file
    def last_used_address(self):
        print('last used')
        with open('./usedAddresses.json', 'r') as f:
            read_file = json.load(f)
            last_used_address = read_file['usedAddresses']['ids'][-1]['address']
            self.file_index = len(read_file['usedAddresses']['ids'])

            print('This was used last: ', self.last_index, last_used_address)
            print(self.file_index)
            iota_ctrl = IotaControlClass.IotaCtrl()
            iota_ctrl.generate_new_address()

    # write new address to usedAddresses json file
    def write_json(self):
        iota_ctrl = IotaControlClass.IotaCtrl()
        new_id = iota_ctrl.index
        new_spent = iota_ctrl.spent
        new_address = iota_ctrl.new_address
        print(new_spent)
        # with open('./usedAddresses.json', 'r') as r:
        #     dump_file = json.load(r)
        # add_to_json = {'id': new_id, 'spent': new_spent, 'address': new_address}
        # dump_file['usedAddresses']['ids'].append(add_to_json)
        # with open('./usedAddresses.json', 'w') as f:
        #     json.dump(dump_file, f, indent=2)
        #
        # print('This is what we dump: ', new_id, new_spent, new_address)
