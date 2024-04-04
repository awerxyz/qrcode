from utils import clear_entry_widgets

class EntryManager:
    def __init__(self, entry_widgets):
        self.entry_widgets = entry_widgets

    def clear_entries(self):
        clear_entry_widgets(self.entry_widgets)