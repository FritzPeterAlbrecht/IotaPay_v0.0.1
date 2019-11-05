##> Import default!
import sys

##> Import external!
from PyQt5 import QtWidgets

##> Import own classes!
from Configuration import Configuration
from FSend import FSend
from GUI import GUI
from IotaControl import IotaControl
from JsonHandler import JsonHandler
from QRCode import QRCode
from ZMQ import ZMQ
from Timer import Timer

##> Run program!
if __name__ == '__main__':

	##> Setup!
	c = Configuration("./config.json")
	a = QtWidgets.QApplication(sys.argv)
	hj = JsonHandler(c.getJsonPath())
	ic = IotaControl(c, hj, index=0)
	#ic.generate_new_address() # uncomment for startup / or deleted usedAddresses json
	fs = FSend(c, hj.get_last_index(), c.getJsonPath())
	#fs.get_value_addresses() ##> zum testen von Fsend
	qr = QRCode(hj.last_used_address())
	qr.qrCode()
	z = ZMQ(hj.last_used_address())
	t = Timer(z.value, c.getPrice())
	g = GUI(c.getUiPath(), hj, t, z)

	##> Run!
	g.show()
	a.exec()
	sys.exit() ##> Quit after window is closed!