import IotaControlClass
import JsonHandlerClass

# load the config file for node settings
def load_config():
    json_handler = JsonHandlerClass.HandleJson()
    json_handler.configuration()
    node_url = json_handler.node_url
    seed = json_handler.seed
    print(node_url, seed)

# generate the first address of the seed and check if it was spent from
def new_address():
    iota_ctrl = IotaControlClass.IotaCtrl()
    iota_ctrl.generate_new_address()

# if json file usedAdresses is not available, create and write the first address into it
def init_used_addresses():
    json_handler = JsonHandlerClass.HandleJson()
    json_handler.construct_json()

if __name__ == '__main__':
    load_config()
    #new_address()
    init_used_addresses()



