import qrcode
from PIL import Image


class QRCode:
    def __init__(self, state):
        self.address = state.last_used_address

    # generate QR Code for the actual address
    def qrCode(self):

        # generate the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=4,
            border=2,
        )
        qr.add_data(self.address)
        qr.make(fit=True)
        img = qr.make_image()
        img.save("./QRAddress.png")
