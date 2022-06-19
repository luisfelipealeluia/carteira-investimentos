import qrcode
import os

def generate_qrcode(data):

    code = qrcode.make(data)
    code.save(os.path.join(os.path.dirname(os.getcwd()), "temp", "qrcode.png"))

