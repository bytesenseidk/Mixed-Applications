import io
import png
import pyqrcode
from barcode import EAN13
from barcode.writer import ImageWriter
from PIL import Image

class BarCode(object):
    def __init__(self, data):
        if len(data) == 12 and data.isdigit():
            self.data = str(data)
        else:
            self.data = "123456789012"
        
    def generate(self):
        temp = io.BytesIO()
        EAN13(self.data, writer=ImageWriter()).write(temp)
        image = Image.open(temp).resize((400,400), Image.ANTIALIAS)
        image.show()


class QrCode(object):
    def __init__(self, data):
        self.data = data
    
    def generate(self):
        temp = io.BytesIO()
        qr_code = pyqrcode.create(self.data)
        qr_code.png("temp, scale=10")
        # image = Image.open(temp).resize((400,400), Image.ANTIALIAS)
        # image = image.resize((400,400), Image.ANTIALIAS)
        # image.show()
        
    

temp = BarCode("123456789012")
temp = QrCode("123456789012")
temp.generate()