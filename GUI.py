from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from PyQt5.QtGui import QIcon, QPixmap
import sys
import time

class GUI(QtWidgets.QWidget):

	def __init__(self, uiPath, parent=None):
		super(GUI, self).__init__(parent)
		self.uiPath = uiPath
		self.callback = CallbackObject(parent=parent)
		
		uic.loadUi(self.uiPath, self) ##> Load UI from spec file!

		self.threader = UiThreads(self.callback)
		self.threader.start()

#		self.info = 'Welcome to IotaPay.'

		self.info_label = self.findChild(QtWidgets.QLabel, 'info_lbl')
		self.lcd_ui = self.findChild(QtWidgets.QLCDNumber, 'lcd_nr')

		# create CallbackObject and connect signals to slots
		
#		self.callback.signal_info.connect(self.threader)
#		self.callback.signal_lcd.connect(self.threader)

		self.updateUi()

	# update the UI
	def updateUi(self):
		self.info_label.setText('Welcome to IotaPay.')
		print('push Info')
		self.lcd_ui.display("1")
		print('push LCD')


	def start(self):
		a = QtWidgets.QApplication(sys.argv)
		app = GUI()
		app.show()
		sys.exit(a.exec())


# Thread Class
class UiThreads(QtCore.QThread):
	def __init__(self, callback, parent=None):
		super(UiThreads, self).__init__(parent)
		self.callback = callback

	def run(self):
		while True:
#			info = IC.info
#			lcd = IC.txValue
#			self.callback.triggerSignal()
#			self.callback.signal_info.emit('SIGNAL_INFO')
#			self.updater(self)
#			IotaPay.txValue = IotaPay.txValue + 1
			print('threads running')
			time.sleep(0.5)

# def start():
#	  a = QtWidgets.QApplication(sys.argv)
#	  app = UiIotaPay()
#	  app.show()
#	  sys.exit(a.exec())





# create Signals
class CallbackObject(QObject):
	signal_info = pyqtSignal(str, name='SIGNAL_INFO')
	signal_lcd = pyqtSignal(int, name='SIGNAL_LCD')

	def __init__(self, parent):
		super().__init__(parent=parent)
		self.triggerSignal()

	def triggerSignal(self):
		self.signal_info.emit('SIGNAL_INFO')
		print('Info Triggered!')
		self.signal_lcd.emit('SIGNAL_LCD')
		print('LCD Triggered!')
