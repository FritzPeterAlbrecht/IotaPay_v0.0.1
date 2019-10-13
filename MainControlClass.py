import IotaControlClass
import JsonHandlerClass


def load_config():
    json_handler = JsonHandlerClass.HandleJson()
    json_handler.configuration()
    node_url = json_handler.node_url
    seed = json_handler.seed
    print(node_url, seed)


def new_address():
    iota_ctrl = IotaControlClass.IotaCtrl()
    iota_ctrl.generate_new_address()



load_config()
new_address()


