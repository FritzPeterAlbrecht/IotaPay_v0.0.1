from iota import Iota
import JsonHandlerClass


class IotaCtrl:
    def __init__(self):
        json_handler = JsonHandlerClass.HandleJson()
        json_handler.configuration()
        self.node_url = json_handler.node_url
        self.seed = json_handler.seed
        self.index = 0
        self.sec_level = json_handler.sec_level
        self.check_sum = json_handler.check_sum

    def generate_new_address(self):
        print('generator running')
        api = Iota(self.node_url, self.seed)
        self.new_address = api.get_new_addresses(index=self.index, count=1, security_level=self.sec_level,
                                                 checksum=self.check_sum)
        print(self.new_address)