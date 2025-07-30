"""
CP1404/CP5632 Practical
Kivy GUI to convert miles to kilometers
Stephen Yamashita
Started 13/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

CONVERSION_RATE = 1.60934


class ConvertMilesToKmApp(App):

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (600, 400)
        self.title = "Convert miles to km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self, value):
        """Convert miles to kilometers from input when called and place output in label."""
        try:
            result = float(value) * CONVERSION_RATE
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = str(0.0)

    def handle_increment(self, number_input, increment):
        """Increment the value by input number."""
        number_converted = int(number_input)
        result = number_converted + increment
        self.root.ids.input_label.text = str(result)


ConvertMilesToKmApp().run()
