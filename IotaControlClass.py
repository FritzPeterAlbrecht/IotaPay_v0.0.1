from iota import Iota
import JsonHandlerClass


class IotaCtrl:
    def __init__(self):
        #pass
        json_handler = JsonHandlerClass.HandleJson()
        node_url = json_handler.node_url
        self.node_url = node_url
        self.seed = json_handler.seed
        self.index = 0
        self.sec_level = json_handler.sec_level
        self.check_sum = json_handler.check_sum

    def generate_new_address(self, node_url, seed, index, sec_level, check_sum):
        print('generator running')
        start_conf = JsonHandlerClass
        json_handler = start_conf.HandleJson()
        json_handler.node_url()
        api = Iota(node_url, seed)
        api.get_new_addresses(index=index, count=1, security_level=sec_level, checksum=check_sum)

