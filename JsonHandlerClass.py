import json
import IotaControlClass


class HandleJson:
    def __init__(self):
        pass

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
        self.index = iota_ctrl.index

        addressData = {'usedAddresses': {}}
        addressData['usedAddresses']['ids'] = []
        addressData['usedAddresses']['ids'].append({
            "id": self.index,
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
        with open('./usedAddresses.json', 'r') as f:
            read_file = json.load(f)
            last_used_address = read_file['usedAddresses']['ids'][-1]['address']
            print(last_used_address)