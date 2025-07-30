from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.label import Label


class DynamicWidgets(App):
    """Main Program - Kivy app to demonstrate dynamic widget creation"""
    def __init__(self, **kwargs):
        """Construct the main app."""
        super().__init__(**kwargs)
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        """Build the Kivy app through functions in python."""
        Window.size = (600, 400)
        self.title = 'Dynamic Widgets'
        self.root = Builder.load_file('dynamic_widgets.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create widgets dynamically from give data."""
        for entry in self.name_to_phone:
            temp_label = Label(text=entry)
            self.root.ids.main.add_widget(temp_label)


DynamicWidgets().run()
