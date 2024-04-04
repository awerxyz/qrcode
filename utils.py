import qrcode
from PIL import ImageTk


def generate_qr_code(data, options):
    qr = qrcode.QRCode(box_size=int(options["box_size"]), border=int(options["quiet_zone"]))
    qr.add_data(data)
    qr.make(fit=True)
    qrcode.make(data)
    qr_img = qr.make_image(fill_color=options["fill_color"], back_color=options["back_color"])
    tk_image = ImageTk.PhotoImage(qr_img)
    return tk_image

def clear():
    pass