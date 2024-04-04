# handle the "Generate" button 
from tkinter import messagebox
from utils import generate_qr_code

from tkinter import filedialog

class QRGenerator:
    def __init__(self, data_entry, color_entry, background_color_entry, tile_size_entry, quiet_zone_entry, preview_label):
        self.data_entry = data_entry
        self.color_entry = color_entry
        self.background_color_entry = background_color_entry
        self.tile_size_entry = tile_size_entry
        self.quiet_zone_entry = quiet_zone_entry
        self.preview_label = preview_label

    def generate(self):
        data = self.data_entry.get()
        fill_color = self.color_entry.get()
        back_color = self.background_color_entry.get()
        box_size = self.tile_size_entry.get()
        quiet_zone = self.quiet_zone_entry.get()

        try:
            if data:
                options = {
                    "fill_color": fill_color if fill_color else "black",
                    "back_color": back_color if back_color else "white",
                    "box_size": box_size if box_size else 10,
                    "quiet_zone": quiet_zone if quiet_zone else 4
                }

                tk_image = generate_qr_code(data, options)
                self.preview_label.config(image=tk_image)
                self.preview_label.image = tk_image
            else:
                messagebox.showwarning("No Data Entered", "Please enter data in order to generate a QR code.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter valid color name or hex code.\nBox size and quiet zone must be integers.")
            return
    # method for saving the generated image
    def save_qr_code(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            qr_img = self.preview_label.image
            qr_img = qr_img._PhotoImage__photo.subsample(3)  # Adjust subsampling factor as needed
            qr_img.write(file_path)
            messagebox.showinfo("Save Successful", "QR code saved successfully.")