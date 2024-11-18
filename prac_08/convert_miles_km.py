"""
CP1404 - Practical 08: Convert Miles to Km
Ashton Stewart
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

multiplier = 1.60934

class DistanceConverterLayout(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('convert_miles_km.kv')
        #Window.size = (750, 500)
        return self.root

    def convert_distance(self, value):
        """Converts the user input into an output"""
        try:
            distance = float(value)
            distance *= multiplier
            self.root.ids.output_distance.text = str(distance)

        except ValueError:
            self.root.ids.output_distance.text = str(0)

    def input_change(self, value, action):
        """Changes input value based on the pressed button"""
        try:
            distance = float(value)
            if action == "add":
                distance += 1
            else:
                distance -= 1

            self.root.ids.input_number.text = str(distance)

        except ValueError:
            self.root.ids.output_distance.text = str(0)

DistanceConverterLayout().run()
