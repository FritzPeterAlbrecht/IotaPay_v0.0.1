import json


class JsonHandler:
    def __init__(self, jspath):
        self.jspath = jspath

    # If not get first address and write json file
    def construct_json(self, no, spent, address):

        addressData = {"usedAddresses": {}}
        addressData["usedAddresses"]["ids"] = []
        addressData["usedAddresses"]["ids"].append(
            {"id": no, "spent": spent, "address": address}
        )

        with open(self.jspath, "w") as f:
            json.dump(addressData, f, indent=2)
        print("file construction initiated and saved!")

    # get last used address from file
    def last_used_address(self):
        print("reading last used...")
        with open(self.jspath, "r") as f:
            r = json.load(f)
            last_index = self.get_last_index()
            last_address = r["usedAddresses"]["ids"][last_index]["address"]
            return last_address

    # get last used index
    def get_last_index(self):
        print("getting last index...")
        with open(self.jspath, "r") as f:
            r = json.load(f)
            self.index = len(r["usedAddresses"]["ids"]) - 1
            return self.index

    # write new address to usedAddresses json file
    def write_json(self, no, spent, address):

        with open(self.jspath, "r") as r:
            d = json.load(r)

        add_to_json = {"id": no, "spent": spent, "address": address}
        d["usedAddresses"]["ids"].append(add_to_json)
        with open(self.jspath, "w") as f:
            json.dump(d, f, indent=2)
