##> Import default!
import sys

##> Import external!
from PyQt5 import QtWidgets

##> Import own classes!
from Configuration import Configuration
from FSend import FSend
from State import State
from GUI import GUI
from IotaController import IotaController
from JsonHandler import JsonHandler
from QRCode import QRCode
from ZMQ import ZMQ
from Timer import Timer

##> Run program!
if __name__ == "__main__":

    ##> Setup!
    c = Configuration("./config.json")
    a = QtWidgets.QApplication(sys.argv)
    hj = JsonHandler(c.getJsonPath())
    ic = IotaController(c, hj)
    # ic.generate_new_address()  # uncomment for startup / or deleted usedAddresses json
    # fs = FSend(c, hj.get_last_index(), c.getJsonPath())
    # fs.get_value_addresses() ##> zum testen von Fsend - DONT USE IN DEVNET MODE!!!
    qr = QRCode()
    state = State(c, ic, qr)
    z = ZMQ(state)
    t = Timer(state)
    g = GUI(c, hj, t, z, state)

    ##> Run!
    g.show()
    a.exec()
    sys.exit()  ##> Quit after window is closed!

