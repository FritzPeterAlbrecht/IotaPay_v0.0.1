import IotaControlClass
import JsonHandlerClass
import os.path

from Configuration import Configuration


# generate the first address of the seed and check if it was spent from
def new_address():
    iota_ctrl = IotaControlClass.IotaCtrl()
    iota_ctrl.generate_new_address()


# if json file usedAddresses is not available, create and write the first address into it
# def init_used_addresses():
#     json_handler = JsonHandlerClass.HandleJson()
#     json_handler.construct_json()


# check existence of usedAddresses json file. Read if existing, write if not existing
def file_exists():
    if os.path.isfile('./usedAddresses.json'):
        print('file exists')
        json_handler = JsonHandlerClass.HandleJson()
        json_handler.last_used_address()
    else:
        print('file does not exist, initiating...')
        json_handler = JsonHandlerClass.HandleJson()
        json_handler.construct_json()


# QR code generator
def generate_qr():
    pass


if __name__ == '__main__':
	c = Configuration("./node_config.json")
	#print(c.getSeed()) #uncomment to test config
    #file_exists()
	
	##> Benutz doch https://docs.iota.org/docs/node-software/0.1/iri/references/api-reference#wereaddressesspentfrom anstatt eine eigene Lösung aufzuziehen :)
