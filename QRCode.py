import qrcode
from PIL import Image


class QRCode:
    def __init__(self):
        ()

    # generate QR Code for the actual address
    def qrCode(self, address):

        # generate the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=4,
            border=2,
        )
        qr.add_data(address)
        qr.make(fit=True)
        img = qr.make_image()
        img.save("./QRAddress.png")
