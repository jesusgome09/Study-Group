import qrcode
import os

absolutepath = os.path.abspath(__file__)
path, filename = os.path.split(absolutepath)
path = path + "\\"


def make_qr(informacion):
    if informacion != "":
        qrcode.make(informacion).save(path + "QR.png")
        return path + "QR.png"
    else:
        return False


