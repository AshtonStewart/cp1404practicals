"""
CP1404 - Practical 08: Convert Miles to Km
Ashton Stewart
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class DistanceConverterLayout(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert_distance(self, value):

        try:
            distance = float(value)
            distance *= 1.6
            self.root.ids.output_distance.text = str(distance)

        except ValueError:
            self.root.ids.output_distance.text = "Invalid Distance"

DistanceConverterLayout().run()
