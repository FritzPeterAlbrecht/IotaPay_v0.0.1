##> Import default!
import sys

##> Import external!
from PyQt5 import QtWidgets

##> Import own classes!
from Configuration import Configuration
from GUI import GUI
from IotaControl import IotaControl
from JsonHandler import JsonHandler
from QRCode import QRCode
from Timer import Timer

##> Run program!
if __name__ == '__main__':

	##> Setup!
	c = Configuration("./config.json")
	a = QtWidgets.QApplication(sys.argv)
	hj = JsonHandler(c.getJsonPath())
	ic = IotaControl(c, hj, index=0)
	qr = QRCode(hj.last_used_address())
	qr.qrCode()
	t = Timer(500, c.getPrice())
	g = GUI(c.getUiPath(), hj, t)
	#ic.test_looper(t=5) # uncomment for looping address generation and saving

	
	##> Run!
	g.show()
	a.exec()
	sys.exit() ##> Quit after window is closed!