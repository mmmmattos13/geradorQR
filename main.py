import pyqrcode
import png
from pyqrcode import QRCode

s = input("Insira o site para gerar o QRCode: ")
url = pyqrcode.create(s)
url.svg("myqr.svg", scale = 8)
url.png("myqr.png", scale = 6)
