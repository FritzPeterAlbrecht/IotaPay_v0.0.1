##> Import default!
import sys

##> Import external!
from PyQt5 import QtWidgets

##> Import own classes!
from Configuration import Configuration
from GUI import GUI
from IotaControl import IotaControl
from JsonHandler import JsonHandler

##> Run program!
if __name__ == '__main__':

	##> Setup!
	c = Configuration("./config.json")
	a = QtWidgets.QApplication(sys.argv)
	g = GUI(c.getUiPath())
	hj = JsonHandler()
	ic = IotaControl(c, hj, index=0)
	ic.test_looper(t=5)
	
	##> Run!
	g.show()
	a.exec()
	sys.exit() ##> Quit after window is closed!