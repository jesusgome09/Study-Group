import qrcode
import os
import cv2



absolutepath = os.path.abspath(__file__)
path, filename = os.path.split(absolutepath)
path = path + "\\"


def make_qr(informacion):
    if informacion != "":
        qrcode.make(informacion).save(path + "QR.png")
        return path + "QR.png"
    else:
        return False

def read_qr(ubicacion_de_imagen):
    imagen = cv2.imread(ubicacion_de_imagen)

    detector = cv2.QRCodeDetector()

    datos, sera, nada2 = detector.detectAndDecode(imagen)

    if sera is not None:
        return datos

    else:
        return "Esta imagen no es un codigo QR valido"
