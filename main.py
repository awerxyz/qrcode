"""This file contains the entry point for the QR Code Generator application.

.. include:: README.md

"""
import tkinter as tk
from app import QRCodeGeneratorApp


def main():
    """Entry point for the QR Code Generator application.

    Initializes the main Tkinter root window.
    Also initializes the QRCodeGeneratorApp instance.
    Enters the Tkinter event loop to start the application.

    Returns
    -------
    None
    """
    root = tk.Tk()
    QRCodeGeneratorApp(root)
    root.mainloop()


if __name__ == "__main__":
    """Entry point for the application execution.

    This block of code checks if the script is being run as the main program.
    If it is, the `main()` function is called to start the application.

    """
    main()
