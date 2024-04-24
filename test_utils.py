import pytest
import tkinter as tk
from utils import clear_entry_widgets

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