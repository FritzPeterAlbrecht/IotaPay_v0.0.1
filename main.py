# Import default!
import sys

# Import external!
from PyQt5 import QtWidgets

# Import own classes!
from Configuration import Configuration
from FSend import FSend
from State import State
from GUI import GUI
from IotaController import IotaController
from JsonHandler import JsonHandler
from QRCode import QRCode
from ZMQ import ZMQ
from Timer import Timer

# Run program
if __name__ == "__main__":

    # Setup
    config = Configuration("./config.json")
    app = QtWidgets.QApplication(sys.argv)
    filehandler = JsonHandler(config.getJsonPath())
    controller = IotaController(config, filehandler)
    # controller.generate_new_address()  # uncomment for startup / or deleted usedAddresses json
    # fs = FSend(config, filehandler.get_last_index(), config.getJsonPath())
    # fs.get_value_addresses() # just for testing Fsend - DONT USE IN DEVNET MODE!!!
    qr = QRCode(config.getQrPath())
    state = State(config.getPrice(), filehandler, controller, qr)
    listener = ZMQ(state)
    timer = Timer(state)
    gui = GUI(config, filehandler, timer, listener, state)

    # Run
    gui.show()
    app.exec()
    sys.exit()  # Quit after window is closed!

