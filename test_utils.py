import pytest
import tkinter as tk
from utils import clear_entry_widgets, generate_qr_code

def test_generate_qr_code():
    """Test the generate_qr_code function.

    This function tests the generate_qr_code function from utils.py.
    It creates a temporary Tkinter root window, defines sample data and options,
    calls generate_qr_code to generate a QR code, and then checks if the returned
    Tkinter PhotoImage object is not None.

    Returns
    -------
    None
    """
    root = tk.Tk()

    data = "https://www.example.com"
    options = {
        "fill_color": "black",
        "back_color": "white",
        "box_size": 10,
        "quiet_zone": 4
    }

    tk_image = generate_qr_code(data, options)

    assert tk_image is not None

    root.destroy()

def test_clear_entry_widgets():
    """Test the clear_entry_widgets function.

    This function tests the clear_entry_widgets function from utils.py.
    It creates sample Tkinter Entry widgets, sets initial text in them,
    calls clear_entry_widgets to clear the text, and then checks if the
    widgets are cleared as expected.

    Returns
    -------
    None
    """
    root = tk.Tk()
    entry1 = tk.Entry(root)
    entry2 = tk.Entry(root)
    entry3 = tk.Entry(root)

    entry1.insert(0, "Sample Text 1")
    entry2.insert(0, "Sample Text 2")
    entry3.insert(0, "Sample Text 3")

    entry_widgets = [entry1, entry2, entry3]

    clear_entry_widgets(entry_widgets)

    assert entry1.get() == ""
    assert entry2.get() == ""
    assert entry3.get() == ""

    root.destroy()