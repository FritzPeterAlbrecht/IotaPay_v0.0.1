from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from PyQt5.QtGui import QIcon, QPixmap
import sys
import time


class GUI(QtWidgets.QWidget):

	def __init__(self, uiPath, hj, t, parent=None):
		super(GUI, self).__init__(parent)
		self.uiPath = uiPath
		self.callback = CallbackObject(parent=parent)
		self.json = hj
		self.timer = t

		uic.loadUi(self.uiPath, self)  ##> Load UI from spec file!

		self.threader = UiThreads(self.callback, t)
		self.threader.start()

		self.info_label = self.findChild(QtWidgets.QLabel, 'info_lbl')
		self.lcd_ui = self.findChild(QtWidgets.QLCDNumber, 'lcd_nr')

		# create CallbackObject and connect signals to slots
		self.callback.signal_info.connect(self.updateUi)
		self.callback.signal_lcd.connect(self.updateUi)

	# update the UI
	def updateUi(self):
		# set the text for info field in GUI
		self.json.last_used_address()
		self.last_used = str(self.json.last_address[0:41] + '\n' + self.json.last_address[
			42:81] + '\n' + 'CHECKSUM: ' + self.json.last_address[82:91])

		self.info_label.setText(self.last_used)
		print('push Info')

		# set LCD Display in GUI
		self.value = self.timer.stop

		self.lcd_ui.display(str(self.value))
		print('push LCD')


# Thread Class
class UiThreads(QtCore.QThread):
	def __init__(self, callback, t, parent=None):
		super(UiThreads, self).__init__(parent)
		self.callback = callback

	def run(self):

		while True:
			self.callback.triggerSignal() # comment/uncomment to push changes to the GUI
			time.sleep(0.5)


# create Signals
class CallbackObject(QObject):

	signal_info = pyqtSignal(str, name='SIGNAL_INFO')
	signal_lcd = pyqtSignal(int, name='SIGNAL_LCD')

	def __init__(self, parent):
		super().__init__(parent=parent)
		self.triggerSignal()

	def triggerSignal(self):
		self.signal_info.emit('SIGNAL_INFO')
		#print('Info Triggered!')
		self.signal_lcd.emit('SIGNAL_LCD')
		print('LCD Triggered!')
