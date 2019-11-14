from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from PyQt5.QtGui import QIcon, QPixmap
import sys
import time


class GUI(QtWidgets.QWidget):
    def __init__(self, uiPath, hj, t, z, state, parent=None):
        super(GUI, self).__init__(parent)
        self.uiPath = uiPath
        self.callback = CallbackObject(parent=parent)
        self.json = hj
        self.timer = t
        self.zmq = z
        self.state = state

        uic.loadUi(self.uiPath, self)  ##> Load UI from spec file!

        self.threader = UiThreads(self.callback, t, z, state)
        self.threader.start()

        self.info_label = self.findChild(QtWidgets.QLabel, "info_lbl")
        self.lcd_ui = self.findChild(QtWidgets.QLCDNumber, "lcd_nr")

        # create CallbackObject and connect signals to slots
        self.callback.signal_info.connect(self.updateUi)
        self.callback.signal_lcd.connect(self.updateUi)

    # update the UI
    def updateUi(self):
        # set Info Label in GUI
        self.info_label.setText(self.state.message)
        # print("push Info")

        # set LCD Display in GUI
        self.value = self.timer.stop
        self.lcd_ui.display(str(self.value))
        # print("push LCD")


# Thread Class
class UiThreads(QtCore.QThread):
    def __init__(self, callback, t, z, state, parent=None):
        super(UiThreads, self).__init__(parent)
        self.callback = callback
        self.zmq = z
        self.state = state

    def run(self):

        ############################################################
        ##                      MAIN LOOP                         ##
        ############################################################

        while True:
            self.callback.signal_info.emit("SIGNAL_INFO")
            # print("Info Triggered!")
            self.callback.signal_lcd.emit("SIGNAL_LCD")

            # ready - listeing
            if self.state.current == 0:
                self.zmq.listen()
            # tx issued - waiting for confirmaton
            if self.state.current == 1:
                self.zmq.check_confirmation()
            # paymend confirmed - busy/working
            if self.state.current == 2:
                time.sleep(1.0)
                print("Im busy")


# create Signals
class CallbackObject(QObject):

    signal_info = pyqtSignal(str, name="SIGNAL_INFO")
    signal_lcd = pyqtSignal(int, name="SIGNAL_LCD")

    def __init__(self, parent):
        super().__init__(parent=parent)
