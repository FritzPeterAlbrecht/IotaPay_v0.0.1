from JsonHandlerClass import HandleJson
import os.path
import Timer
from Configuration import Configuration


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
    t = Timer.Timer(3)
    t.timer()
    #print(c.getSeed()) #uncomment to test config