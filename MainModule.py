from IotaControlClass import IotaCtrl
from JsonHandlerClass import HandleJson
import os.path

from Configuration import Configuration


# generate the first address of the seed and check if it was spent from
def new_address():
    ic = IotaCtrl()
    ic.generate_new_address()


# check existence of usedAddresses json file. Read if existing, write if not existing
def file_exists():
    if os.path.isfile('./usedAddresses.json'):
        print('file exists')
        jh = HandleJson()
        jh.last_used_address()
    else:
        print('file does not exist, initiating...')
        jh = HandleJson()
        jh.construct_json()


if __name__ == '__main__':
    c = Configuration("./node_config.json")
    file_exists()
    #generate_qr()

	#print(c.getSeed()) #uncomment to test config
	##> Benutz doch https://docs.iota.org/docs/node-software/0.1/iri/references/api-reference#wereaddressesspentfrom anstatt eine eigene Lösung aufzuziehen :)
