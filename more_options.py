# handle the "More Options" button

class MoreOptions:
    def __init__(self, options_frame, more_options_button):
        self.options_frame = options_frame
        self.more_options_button = more_options_button

    def toggle_options(self):
        if (self.options_frame.winfo_ismapped()):
            self.options_frame.pack_forget()
            self.more_options_button.config(text="More Options")
        else:
            self.options_frame.pack()
            self.more_options_button.config(text="Less Options")