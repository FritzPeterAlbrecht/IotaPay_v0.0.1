from IotaControlClass import IotaCtrl as IC
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import (Qt, pyqtSignal, QObject)
from PyQt5.QtGui import QIcon, QPixmap
import sys


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


# UI Class
class UiIotaPay(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(UiIotaPay, self).__init__(parent)
        uic.loadUi('./IotaPayV001.ui', self)

        self.threader = UiThreads()
        self.threader.start()

        self.info = IC.info

        self.info_label = self.findChild(QtWidgets.QLabel, 'info_lbl')
        self.lcd_ui = self.findChild(QtWidgets.QLCDNumber, 'lcd_nr')

        # create CallbackObject and connect signals to slots
        self._callback = CallbackObject(parent=parent)
        self._callback.signal_info.connect(UiThreads)
        self._callback.signal_lcd.connect(UiThreads)

        self.updateUi()

    # update the UI
    def updateUi(self):
        self.info_label.setText(IC.info)
        print('push Info')
        self.lcd_ui.display(IC.txValue)
        print('push LCD')

    def start(self):
        a = QtWidgets.QApplication(sys.argv)
        app = UiIotaPay()
        app.show()
        sys.exit(a.exec())


# Thread Class
class UiThreads(QtCore.QThread):
    def __init__(self, parent=None):
        super(UiThreads, self).__init__(parent)

    def run(self):

        while 1:
            info = IC.info
            lcd = IC.txValue
            app._callback.triggerSignal()
            #CallbackObject.signal_info.emit('SIGNAL_INFO')
            #self.updater(self)
            IotaPay.txValue = IotaPay.txValue + 1
            print('threads running', IotaPay.txValue)
            time.sleep(0.5)

# def start():
#     a = QtWidgets.QApplication(sys.argv)
#     app = UiIotaPay()
#     app.show()
#     sys.exit(a.exec())
