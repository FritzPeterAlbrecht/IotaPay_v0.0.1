import json


class JsonHandler:

    def __init__(self):
        pass

    # If not get first address and write json file
    def construct_json(self, no, spent, address):

        addressData = {'usedAddresses': {}}
        addressData['usedAddresses']['ids'] = []
        addressData['usedAddresses']['ids'].append({
            "id": no,
            "spent": spent,
            "address": address
        })

        with open('./usedAddresses.json', 'w') as f:
            json.dump(addressData, f, indent=2)
        print('file construction initiated and saved!')

    # get last used address from file to set index
    def last_used_address(self):
        print('reading last used...')
        with open("./usedAddresses.json", "r") as f:
            r = json.load(f)
            self.last_address = str(r["usedAddresses"]["ids"][-1])
            self.file_index = len(r['usedAddresses']['ids'])
            self.index = self.file_index

    # write new address to usedAddresses json file
    def write_json(self, no, spent, address):

        with open('./usedAddresses.json', 'r') as r:
            d = json.load(r)
            self.file_index = len(d['usedAddresses']['ids'])

        add_to_json = {
            'id': no,
            'spent': spent,
            'address': address
        }
        d['usedAddresses']['ids'].append(add_to_json)
        with open('./usedAddresses.json', 'w') as f:
            json.dump(d, f, indent=2)

        print('This is what we dump: ', no, spent, address)
