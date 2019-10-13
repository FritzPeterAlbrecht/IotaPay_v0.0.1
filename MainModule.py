import IotaControlClass
import JsonHandlerClass
import os.path


# load the config file for node settings
def load_config():
    json_handler = JsonHandlerClass.HandleJson()
    json_handler.configuration()
    node_url = json_handler.node_url
    seed = json_handler.seed
    # print(node_url, seed)


# generate the first address of the seed and check if it was spent from
def new_address():
    iota_ctrl = IotaControlClass.IotaCtrl()
    iota_ctrl.generate_new_address()


# if json file usedAddresses is not available, create and write the first address into it
def init_used_addresses():
    json_handler = JsonHandlerClass.HandleJson()
    json_handler.construct_json()


# check existence of usedAddresses json file. Read if existing, write if not existing
def file_exists():
    print('file exists')
    if os.path.isfile('./usedAddresses.json'):
        json_handler = JsonHandlerClass.HandleJson()
        json_handler.last_used_address()
    else:
        init_used_addresses()


# QR code generator
def generate_qr():
    pass


if __name__ == '__main__':
    load_config()
    file_exists()
