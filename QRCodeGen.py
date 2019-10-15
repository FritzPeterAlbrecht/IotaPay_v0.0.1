import JsonHandlerClass
import qrcode
from PIL import Image


class QRCodeGen:

    def __init__(self):
        pass

    # generate QR Code for the actual address
    def qrCode(self, address):
        print('generating QR C0d3')

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=4,
            border=2,
        )
        qr.add_data(self, address)
        qr.make(fit=False)
        img = qr.make_image()
        img.save('./QRAddress.png')
