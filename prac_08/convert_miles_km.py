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
        distance = float(value)
        distance *= 1.6
        #distance = self.root.ids.input_name.text
        #result = float(value) ** 2
        self.root.ids.output_distance.text = str(distance)
        print(distance)

DistanceConverterLayout().run()
