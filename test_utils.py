import pytest
import tkinter as tk
from utils import clear_entry_widgets, generate_qr_code

def test_generate_qr_code():
    # Initialize a temporary Tkinter root window
    root = tk.Tk()

    # Sample data and options
    data = "https://www.example.com"
    options = {
        "fill_color": "black",
        "back_color": "white",
        "box_size": 10,
        "quiet_zone": 4
    }

    # Call generate_qr_code function
    tk_image = generate_qr_code(data, options)

    # Check if the returned tk_image is not None
    assert tk_image is not None

    # Destroy the temporary Tkinter root window
    root.destroy()

def test_clear_entry_widgets():
    # Create some sample Entry widgets
    root = tk.Tk()
    entry1 = tk.Entry(root)
    entry2 = tk.Entry(root)
    entry3 = tk.Entry(root)

    # Set some initial text in the Entry widgets
    entry1.insert(0, "Sample Text 1")
    entry2.insert(0, "Sample Text 2")
    entry3.insert(0, "Sample Text 3")

    # List of sample Entry widgets
    entry_widgets = [entry1, entry2, entry3]

    # Call clear_entry_widgets function
    clear_entry_widgets(entry_widgets)

    # Check if the Entry widgets are cleared
    assert entry1.get() == ""
    assert entry2.get() == ""
    assert entry3.get() == ""

    # Destroy the Tkinter root window
    root.destroy()