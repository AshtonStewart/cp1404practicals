"""
CP1404 - Practical 08: Convert Miles to Km
Ashton Stewart
"""


from kivy.app import App
from kivy.lang import Builder

class DistanceConverterLayout(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

DistanceConverterLayout().run()
