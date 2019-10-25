import qrcode
from PIL import Image


class QRCodeGen:

    def __init__(self):
        pass

    # generate QR Code for the actual address
    def qrCode(self, address):
        qraddress = address

        # generate the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=4,
            border=2,
            )
        qr.add_data(qraddress)
        qr.make(fit=True)
        img = qr.make_image()
        img.save('./QRAddress.png')
