import json


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

    def construct_json(self):
        pass
