import json


class HandleJson:
    def __init__(self):
        self.node_url = str()

    def configuration(self):

        with open('./node_config.json', 'r') as f:
            config_file = json.load(f)
            print(config_file)
            self.node_url = config_file['Node']
            seed = config_file['Seed']
            sec_level = config_file['SecurityLevel']
            check_sum = config_file['CheckSum']

    def construct_json(self):
        pass
