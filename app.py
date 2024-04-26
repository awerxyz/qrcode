"""Contains the main application class."""

import tkinter as tk
from styles import style_labels, style_buttons, style_frames, style_entries
from utils import generate_qr_code, clear_entry_widgets
from tkinter import filedialog, messagebox


class QRCodeGeneratorApp:
    """A QR code generator application using tkinter.

    Attributes
    ----------
    root : tk.Tk
        The root window of the application.
    preview_label : tk.Label
        The label for displaying instructions and the QR code.
    data_label : tk.Label
        The label for entering data.
    data_entry : tk.Entry
        The entry widget for data input.
    more_options_button : tk.Button
        The button for toggling additional options.
    options_frame : tk.Frame
        The frame containing additional options.
    color_label : tk.Label
        The label for color input.
    color_entry : tk.Entry
        The entry widget for color input.
    background_color_label : tk.Label
        The label for background color input.
    background_color_entry : tk.Entry
        The entry widget for background color input.
    tile_size_label : tk.Label
        The label for tile size input.
    tile_size_entry : tk.Entry
        The entry widget for tile size input.
    quiet_zone_label : tk.Label
        The label for quiet zone size input.
    quiet_zone_entry : tk.Entry
        The entry widget for quiet zone size input.
    button_frame : tk.Frame
        The frame containing generate, save, and clear buttons.
    generate_button : tk.Button
        The button for generating the QR code.
    save_button : tk.Button
        The button for saving the QR code.
    clear_button : tk.Button
        The button for clearing input fields.
    """

    def __init__(self, root):
        """Initialize the QRCodeGeneratorApp.

        Parameters
        ----------
        root : tk.Tk
            The root window of the application.
        """
        self.root = root
        self.root.title("QR Code Generator")

        self.preview_label = tk.Label(self.root, text="Instructions:"
                                      "\nEnter the data to "
                                      "encode into the QR code."
                                      "\nClick 'Generate' to generate "
                                      "the QR code preview. "
                                      "\n Click "
                                      "'Save' to save the generated "
                                      "picture on your machine.\n")
        self.preview_label.pack(pady=10)

        self.data_label = tk.Label(self.root, text="Enter Data:")
        self.data_label.pack()
        self.data_entry = tk.Entry(self.root)
        self.data_entry.pack(pady=10)

        self.more_options_button = tk.Button(self.root, text="More Options",
                                             command=self.toggle_options)
        self.more_options_button.pack(pady=10)

        self.options_frame = tk.Frame(self.root)

        self.color_label = tk.Label(self.options_frame, text="Color:")
        self.color_label.pack(pady=(0, 10))
        self.color_entry = tk.Entry(self.options_frame)
        self.color_entry.pack(pady=(0, 20))

        self.background_color_label = tk.Label(self.options_frame,
                                               text="Background Color:")
        self.background_color_label.pack(pady=(0, 10))
        self.background_color_entry = tk.Entry(self.options_frame)
        self.background_color_entry.pack(pady=(0, 20))

        self.tile_size_label = tk.Label(self.options_frame,
                                        text="Box size (in pixels):")
        self.tile_size_label.pack(pady=(0, 10))
        self.tile_size_entry = tk.Entry(self.options_frame)
        self.tile_size_entry.pack(pady=(0, 20))

        self.quiet_zone_label = tk.Label(self.options_frame,
                                         text="Quiet zone size (in boxes):")
        self.quiet_zone_label.pack(pady=(0, 10))
        self.quiet_zone_entry = tk.Entry(self.options_frame)
        self.quiet_zone_entry.pack(pady=(0, 20))

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.generate_button = tk.Button(self.button_frame, text="Generate",
                                         command=self.generate)
        self.generate_button.pack(side="left", padx=5, pady=(0, 10))

        self.save_button = tk.Button(self.button_frame, text="Save",
                                     command=self.save)
        self.save_button.pack(side="left", padx=5, pady=(0, 10))

        self.clear_button = tk.Button(self.button_frame, text="Clear",
                                      command=self.clear)
        self.clear_button.pack(side="left", padx=5, pady=(0, 10))

        self.labels = [self.preview_label,
                       self.data_label,
                       self.color_label,
                       self.background_color_label,
                       self.tile_size_label,
                       self.quiet_zone_label]
        style_labels(self.labels)

        self.buttons = [self.more_options_button,
                        self.generate_button,
                        self.save_button,
                        self.clear_button]
        style_buttons(self.buttons)

        self.frames = [self.root,
                       self.options_frame,
                       self.button_frame]
        style_frames(self.frames)

        self.entries = [self.data_entry,
                        self.color_entry,
                        self.background_color_entry,
                        self.tile_size_entry,
                        self.quiet_zone_entry]
        style_entries(self.entries)

    def toggle_options(self):
        """Toggle the display of additional options frame.

        Toggles the display of the additional options frame.
        Updates the text of the more_options_button accordingly.
        """
        if (self.options_frame.winfo_ismapped()):
            self.options_frame.pack_forget()
            self.more_options_button.config(text="More Options")
        else:
            self.options_frame.pack()
            self.more_options_button.config(text="Less Options")

    def generate(self):
        """Generate the QR code based on user input.

        Reads user input to generate a QR code.
        Displays the generated QR code in the preview_label.
        """
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
                messagebox.showwarning("No Data",
                                       "Please enter data in "
                                       "order to generate a QR code.")
        except ValueError:
            messagebox.showerror("Invalid Input",
                                 "Enter valid color name or hex code.\nBox "
                                 "size and quiet zone must be integers.")
            return

    def save(self):
        """Save the generated QR code.

        Allows the user to select a file path.
        """
        try:
            data = self.data_entry.get()
            if data:
                file_path = filedialog.asksaveasfilename(
                        defaultextension=".png",
                        filetypes=[("PNG files", "*.png"),
                                   ("All files", "*.*")])
                if file_path:
                    qr_img = self.preview_label.image
                    qr_img = qr_img._PhotoImage__photo.subsample(3)
                    qr_img.write(file_path)
                    messagebox.showinfo("Save Successful",
                                        "QR code saved successfully.")
            else:
                messagebox.showwarning("No Data",
                                       "Enter data in "
                                       "order to save a QR code.")
        except AttributeError:
            messagebox.showwarning("No QR Code Generated",
                                   "Generate the QR code in order to save it.")

    def clear(self):
        """
        Clear all input fields.

        Clears all the entry widgets in the entries list.
        """
        clear_entry_widgets(self.entries)


if __name__ == "__main__":
    """Main entry point of the application.

    This block of code initializes a Tkinter root window, creates an instance
    of the QRCodeGeneratorApp class
    and starts the Tkinter event loop to handle
    user interactions.

    """
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()
