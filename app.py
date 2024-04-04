import tkinter as tk
from styles import style_labels, style_buttons, style_frames, style_entries
from more_options import MoreOptions
from qr_generator import QRGenerator
from entry_manager import EntryManager

class QRCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")

        # Create a Label to display instructions and QR code preview
        self.preview_label = tk.Label(self.root, text="Instructions:\nEnter the data to encode into the QR code.\nClick 'generate' to generate the QR code preview. \n Click 'save' to save the generated picture on your machine.\n")
        self.preview_label.pack(pady=10)

        # enter data label & field
        self.data_label = tk.Label(self.root, text="Enter Data:")
        self.data_label.pack()
        self.data_entry = tk.Entry(self.root)
        self.data_entry.pack(pady=10)

        # "More Options" button
        self.more_options_button = tk.Button(self.root, text="More Options")
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

        self.tile_size_label = tk.Label(self.options_frame, text="Box size (in pixels):")
        self.tile_size_label.pack(pady=(0,10))
        self.tile_size_entry = tk.Entry(self.options_frame)
        self.tile_size_entry.pack(pady=(0,20))

        self.quiet_zone_label = tk.Label(self.options_frame, text="Quiet zone size (in boxes):")
        self.quiet_zone_label.pack(pady=(0,10))
        self.quiet_zone_entry = tk.Entry(self.options_frame)
        self.quiet_zone_entry.pack(pady=(0,20))

        # frame for Generate, Save, Clear buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        # Generate, Save, Clear buttons
        self.generate_button = tk.Button(self.button_frame, text="Generate")
        self.generate_button.pack(side="left", padx=5, pady=(0,10))

        self.save_button = tk.Button(self.button_frame, text="Save")
        self.save_button.pack(side="left", padx=5, pady=(0,10))

        self.clear_button = tk.Button(self.button_frame, text="Clear")
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

        # instantiate imported classes
        self.more_options = MoreOptions(self.options_frame, self.more_options_button)
        self.more_options_button.config(command=self.more_options.toggle_options)

        self.qr_generator = QRGenerator(self.data_entry, self.color_entry, self.background_color_entry, self.tile_size_entry, self.quiet_zone_entry, self.preview_label)
        self.generate_button.config(command=self.generate_qr_wrapper)

        self.entry_manager = EntryManager([self.data_entry, self.color_entry, self.background_color_entry, self.tile_size_entry, self.quiet_zone_entry])
        self.clear_button.config(command=self.clear_entries)

    # imported methods
    def generate_qr_wrapper(self):
        self.qr_generator.generate()

    def clear_entries(self):
        self.entry_manager.clear_entries()

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()