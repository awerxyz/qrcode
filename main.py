import tkinter as tk
from app import QRCodeGeneratorApp

def main():
    """Entry point for the QR Code Generator application.

    Initializes the main Tkinter root window and the QRCodeGeneratorApp instance.
    Enters the Tkinter event loop to start the application.

    Returns
    -------
    None
    """

    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()