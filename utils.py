"""utils.py

This file contains utility functions for generating QR codes and clearing entry widgets.
"""

import qrcode
from PIL import ImageTk
import tkinter as tk

def generate_qr_code(data, options):
    """Generate a QR code image based on the provided data and options.

    Parameters
    ----------
    data : str
        The data to be encoded into the QR code.
    options : dict
        A dictionary containing the following optional parameters:
        - fill_color : str
            The color of the QR code squares.
        - back_color : str
            The background color of the QR code.
        - box_size : int
            The size of each box in pixels.
        - quiet_zone : int
            The size of the quiet zone in boxes.

    Returns
    -------
    ImageTk.PhotoImage
        A Tkinter PhotoImage object containing the generated QR code.

    Notes
    -----
    The options dictionary can contain keys for 'fill_color', 'back_color',
    'box_size', and 'quiet_zone'. If a key is missing, default values are used.
    """

    qr = qrcode.QRCode(box_size=int(options["box_size"]), border=int(options["quiet_zone"]))
    qr.add_data(data)
    qr.make(fit=True)
    qrcode.make(data)
    qr_img = qr.make_image(fill_color=options["fill_color"], back_color=options["back_color"])
    tk_image = ImageTk.PhotoImage(qr_img)
    return tk_image

def clear_entry_widgets(entry_widgets):
    """Clear the content of a list of Tkinter Entry widgets.

    Parameters
    ----------
    entry_widgets : list
        A list of Tkinter Entry widgets to be cleared.

    Returns
    -------
    None
    """

    for entry_widget in entry_widgets:
        entry_widget.delete(0, tk.END)