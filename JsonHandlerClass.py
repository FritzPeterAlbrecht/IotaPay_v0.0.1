import json

from QRCodeGen import QRCodeGen

class HandleJson:

    def __init__(self):
        pass

    # check if the json file usedAddresses is existing. If not get first address and write json file
    def construct_json(self):
        print('generating first address from seed...')
        ic = IotaControlClass.IotaCtrl()
        ic.generate_new_address(index=0)
        self.first_address = str(ic.new_address)
        self.spent = ic.spent

        addressData = {'usedAddresses': {}}
        addressData['usedAddresses']['ids'] = []
        addressData['usedAddresses']['ids'].append({
            "id": 0,
            "spent": self.spent,
            "address": self.first_address
        })

        with open('./usedAddresses.json', 'w') as f:
            json.dump(addressData, f, indent=2)
        print('file construction initiated and saved!')

        if self.spent is True:
            hj = HandleJson()
            hj.last_used_address()
            print('USED! generating new address...')
        else:
            address = self.first_address
            # generate new Qr Code and save to file
            print('QR: ', address)
            qr = QRCodeGen()
            qr.qrCode(address)

    # get last used address from file to set index
    def last_used_address(self):
        print('reading last used...')
        with open("./usedAddresses.json", "r") as f:
            r = json.load(f)
            self.last_address = str(r["usedAddresses"]["ids"][-1])
            self.file_index = len(r['usedAddresses']['ids'])
            index = self.file_index
            print('file index is: ', self.file_index)

            ic = IotaControlClass.IotaCtrl()
            ic.generate_new_address(index)

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

        # generate new Qr Code and save to file
        print('QR: ', address)
        qr = QRCodeGen()
        qr.qrCode(address)
