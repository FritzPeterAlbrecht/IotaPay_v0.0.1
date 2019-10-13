import IotaControlClass
import JsonHandlerClass


class MainCtrl:
    def __init__(self):
        pass

    def load_config(self):
        start_conf = JsonHandlerClass
        json_handler = start_conf.HandleJson()
        json_handler.configuration()

    def new_address(self):
        new_add = IotaControlClass.IotaCtrl()
        get_add = new_add.generate_new_address()



app = MainCtrl
app.load_config(app)


