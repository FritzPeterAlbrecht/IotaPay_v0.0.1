from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from PyQt5.QtGui import QIcon, QPixmap
#import sys
import time


class GUI(QtWidgets.QWidget):
    def __init__(self, config, filehandler, timer, listener, state, parent=None):
        super(GUI, self).__init__(parent)
        self.uiPath = config.getUiPath()
        self.qrPath = config.getQrPath()
        self.pixmap = QPixmap
        self.callback = CallbackObject(parent=parent)
        self.json = filehandler
        self.timer = timer
        self.listener = listener
        self.state = state

        # load ui file from config
        uic.loadUi(self.uiPath, self)

        # make threader instance
        self.threader = UiThreads(self.callback, timer, listener, state)
        self.threader.start()

        # find the parts of the GUI
        self.info_label = self.findChild(QtWidgets.QLabel, "info_lbl")
        self.lcd_ui = self.findChild(QtWidgets.QLCDNumber, "lcd_nr")
        self.qrcode_label = self.findChild(QtWidgets.QLabel, "qrcode_lbl")

        # create CallbackObject and connect signals to slots
        self.callback.signal_info.connect(self.updateUi)
        self.callback.signal_lcd.connect(self.updateUi)
        self.callback.signal_qrcode.connect(self.updateUi)

    # update the UI
    def updateUi(self):
        # set Info Label in GUI
        self.info_label.setText(self.state.message)

        # set LCD Display in GUI
        self.lcd_ui.display(str(self.timer.duration))

        # set qr code picture to label
        self.qrcode_label.setPixmap(self.pixmap(self.qrPath))


# Thread Class
class UiThreads(QtCore.QThread):
    def __init__(self, callback, timer, listener, state, parent=None):
        super(UiThreads, self).__init__(parent)
        self.callback = callback
        self.listener = listener
        self.timer = timer
        self.state = state

    def run(self):

        ############################################################
        ##                      MAIN LOOP                         ##
        ############################################################

        while True:

            self.callback.signal_info.emit("SIGNAL_INFO")
            self.callback.signal_lcd.emit("SIGNAL_LCD")
            self.callback.signal_qrcode.emit("SIGNAL_QR_CODE")

            # timer ended
            if self.state.current == 4:
                # get next address before changing state
                self.state.next_address()
                self.state.set(0)

                # update qr code
                self.state.update_qr()

            # timer loaded
            if self.state.current == 3:
                time.sleep(1.0)
                self.timer.update()

            # payment confirmed - load timer
            if self.state.current == 2:
                time.sleep(0.2)
                self.timer.setup()
            # tx issued - waiting for confirmation
            if self.state.current == 1:
                self.listener.check_confirmation()
            # ready - listening
            if self.state.current == 0:
                self.listener.listen()


# create Signals
class CallbackObject(QObject):

    signal_info = pyqtSignal(str, name="SIGNAL_INFO")
    signal_lcd = pyqtSignal(int, name="SIGNAL_LCD")
    signal_qrcode = pyqtSignal(int, name="SIGNAL_QR_CODE")

    def __init__(self, parent):
        super().__init__(parent=parent)
