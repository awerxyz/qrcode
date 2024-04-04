# set styles to the widgets

def style_labels(labels):
    for label in labels:
        label.config(fg="white", bg="#15141b")

def style_buttons(buttons):
    for button in buttons:
        button.config(fg="white", bg="#2d1d42", relief="raised", borderwidth=1, highlightbackground="black", activebackground="black", activeforeground="white")

def style_frames(frames):
    for frame in frames:
        frame.config(bg="#110f18")

def style_entries(entries):
    for entry in entries:
        entry.config(bg="#8b84b3")
