"""styles.py

This file contains utility functions for styling tkinter widgets.
"""

def style_labels(labels):
    """Apply styling to a list of Tkinter Label widgets.

    Sets the foreground color to white, and the background color to a dark shade.
    
    Parameters
    ----------
    labels : list
        A list of Tkinter Label widgets to be styled.

    Returns
    -------
    None
    """

    for label in labels:
        label.config(fg="white", bg="#15141b")

def style_buttons(buttons):
    """Apply styling to a list of Tkinter Button widgets.

    Sets the foreground color to white, the background color to a dark shade,
    and adjusts other visual properties for a raised button appearance.

    Parameters
    ----------
    buttons : list
        A list of Tkinter Button widgets to be styled.

    Returns
    -------
    None
    """

    for button in buttons:
        button.config(fg="white", bg="#2d1d42", relief="raised", borderwidth=1, highlightbackground="black", activebackground="black", activeforeground="white")

def style_frames(frames):
    """Apply styling to a list of Tkinter Frame widgets.

    Sets the background color to a dark shade for each frame.

    Parameters
    ----------
    frames : list
        A list of Tkinter Frame widgets to be styled.

    Returns
    -------
    None
    """

    for frame in frames:
        frame.config(bg="#110f18")

def style_entries(entries):
    """Apply styling to a list of Tkinter Entry widgets.

    Sets the background color to a light shade for each entry widget.

    Parameters
    ----------
    entries : list
        A list of Tkinter Entry widgets to be styled.

    Returns
    -------
    None
    """

    for entry in entries:
        entry.config(bg="#8b84b3")