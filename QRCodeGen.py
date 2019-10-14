from JsonHandlerClass import HandleJson
import qrcode


class QRCodeGen:

    def __init__(self):
        hj = HandleJson()
        self.qr_address = hj.last_address

    # generate QR Code for the actual address
    def qrCode(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=4,
            border=2,
        )
        qr.add_data(self.qr_address)
        qr.make(fit=True)
        img = qr.make_image()
        img.save('./QRAddress.png')