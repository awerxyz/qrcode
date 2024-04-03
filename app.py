import tkinter as tk
from tkinter import filedialog
import qrcode
from PIL import ImageTk, Image
from styles import style_labels, style_buttons, style_frames, style_entries

class QRCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")

        # Create a Label to display instructions and QR code preview
        self.preview_label = tk.Label(self.root, text="Instructions:\nEnter the data to encode into the QR code.\nClick 'generate' to generate the QR code preview. \n Click 'save' to save the generated picture on your machine.\n")
        self.preview_label.pack(pady=10)

        '''
        Later, when the user generates the QR code, you can update the text of self.preview_label 
        with the generated QR code image using the configure method: 
            self.preview_label.configure(image=qr_code_image)
        '''
        
        # enter data label & field
        self.data_label = tk.Label(self.root, text="Enter Data:")
        self.data_label.pack()
        self.data_entry = tk.Entry(self.root)
        self.data_entry.pack(pady=10)

        # "More Options" button
        self.more_options_button = tk.Button(self.root, text="More Options", command=self.toggle_options)
        self.more_options_button.pack(pady=10)

        # aditional options frame
        self.options_frame = tk.Frame(self.root)

        self.color_label = tk.Label(self.options_frame, text="Color:")
        self.color_label.pack(pady=(0,10))
        self.color_entry = tk.Entry(self.options_frame)
        self.color_entry.pack(pady=(0,20))

        self.background_color_label = tk.Label(self.options_frame, text="Background Color:")
        self.background_color_label.pack(pady=(0,10))
        self.background_color_entry = tk.Entry(self.options_frame)
        self.background_color_entry.pack(pady=(0,20))

        self.tile_size_label = tk.Label(self.options_frame, text="Tile size:")
        self.tile_size_label.pack(pady=(0,10))
        self.tile_size_entry = tk.Entry(self.options_frame)
        self.tile_size_entry.pack(pady=(0,20))

        self.quiet_zone_label = tk.Label(self.options_frame, text="Quiet zone size:")
        self.quiet_zone_label.pack(pady=(0,10))
        self.quiet_zone_entry = tk.Entry(self.options_frame)
        self.quiet_zone_entry.pack(pady=(0,20))

        # frame for Generate, Save, Clear buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        # Generate, Save, Clear buttons
        self.generate_button = tk.Button(self.button_frame, text="Generate", command=self.generate_qr_code)
        self.generate_button.pack(side="left", padx=5, pady=(0,10))

        self.save_button = tk.Button(self.button_frame, text="Save", command=self.save_qr_code)
        self.save_button.pack(side="left", padx=5, pady=(0,10))

        self.clear_button = tk.Button(self.button_frame, text="Clear", command=self.clear_data)
        self.clear_button.pack(side="left", padx=5, pady=(0,10))

        # styles
        labels = [self.preview_label, self.data_label, self.color_label, self.background_color_label, self.tile_size_label, self.quiet_zone_label]
        style_labels(labels)

        buttons = [self.more_options_button, self.generate_button, self.save_button, self.clear_button]
        style_buttons(buttons)

        frames = [self.root, self.options_frame, self.button_frame]
        style_frames(frames)
        
        entries = [self.data_entry, self.color_entry, self.background_color_entry, self.tile_size_entry, self.quiet_zone_entry]
        style_entries(entries)

    def toggle_options(self):
        if (self.options_frame.winfo_ismapped()):
            self.options_frame.pack_forget()
            self.more_options_button.config(text="More Options")
        else:
            self.options_frame.pack()
            self.more_options_button.config(text="Less Options")

    def generate_qr_code(self):
        # Add logic to generate QR code based on data_entry field
        pass

    def save_qr_code(self):
        # Add logic to save the generated QR code
        pass

    def clear_data(self):
        # Add logic to clear the data_entry field
        pass




























if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()
