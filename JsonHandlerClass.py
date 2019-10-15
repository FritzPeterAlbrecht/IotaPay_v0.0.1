import json
import IotaControlClass


class HandleJson:

    def __init__(self):

        self.last_index = int()
        self.file_index = int()
        self.last_address = str()

    # check if the json file usedAddresses is existing. If not get first address and write json file
    def construct_json(self):
        print('generating first address from seed...')
        ic = IotaControlClass.IotaCtrl()
        ic.generate_new_address()
        self.first_address = str(ic.new_address)
        self.spent = ic.spent

        index = 0

        addressData = {'usedAddresses': {}}
        addressData['usedAddresses']['ids'] = []
        addressData['usedAddresses']['ids'].append({
            "id": index,
            "spent": self.spent,
            "address": self.first_address
        })
        with open('./usedAddresses.json', 'w') as f:
            json.dump(addressData, f, indent=2)
        print('file construction initiated and saved!')
        if self.spent is True:
            print('USED! generating new address...')
            ic.generate_new_address()
        else:
            pass

    # get last used address from file to set index
    def last_used_address(self):
        print('reading last used...')
        with open("./usedAddresses.json", "r") as f:
            r = json.load(f)
            self.last_address = str(r["usedAddresses"]["ids"][-1])
            self.file_index = len(r['usedAddresses']['ids'])
            print('file index is: ', self.file_index, self.last_address)
            ic = IotaControlClass.IotaCtrl()
            ic.index = self.file_index
            ic.generate_new_address()

    # write new address to usedAddresses json file
    def write_json(self):
        with open('./usedAddresses.json', 'r') as r:
            d = json.load(r)
            self.file_index = len(d['usedAddresses']['ids'])

        ic = IotaControlClass.IotaCtrl()
        new_id = self.file_index
        new_spent = ic.spent
        new_address = ic.new_address

        with open('./usedAddresses.json', 'r') as r:
            dump_file = json.load(r)

        add_to_json = {'id': new_id, 'spent': new_spent, 'address': new_address}
        dump_file['usedAddresses']['ids'].append(add_to_json)

        with open('./usedAddresses.json', 'w') as f:
            json.dump(dump_file, f, indent=2)

        print('This is what we dump: ', new_id, new_spent, new_address)
