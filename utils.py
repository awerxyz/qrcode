import qrcode
from PIL import Image

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True) # automatically adjust the size of the code to fit the data

    img = qr.make_image(fill_color="black", back_color="white")
    return img

def save_qr_code(img, filename):
    img.save(filename)
