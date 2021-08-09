import io
from barcode import EAN13
from barcode.writer import ImageWriter
from PIL import Image

class Bar_Gen(object):
    def __init__(self, digits):
        self.bar_image = self.bar_generator(digits)

    @staticmethod
    def bar_generator(digits):
        temp = io.BytesIO()
        EAN13(str(digits), writer=ImageWriter()).write(temp)
        image = Image.open(temp)
        image = image.resize((400,400), Image.ANTIALIAS)
        image.show()


if __name__ == "__main__":
    while True:
        try:
            code = int(input("[BAR] Enter 12 digits: "))
            if code < 12 or code > 12:
                print("Need 12 digits...")
                continue
            else:
                Bar_Gen(code)
                break
        except KeyboardInterrupt:
            break
        except:
            print("need 12 numeric values...")
            continue
        
