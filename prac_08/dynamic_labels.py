"""
CP1404 - Practical 08
Dyanmic Labels
Ashton Stewart
"""

from kivy.app import App
from kivy.lang import Builder

class DynamicLayoutApp(App):
    def build(self):
        self.title = "Dynamic demo"
        self.root = Builder.load_file("dynamic_labels.kv")
        print("test")
        return self.root

DynamicLayoutApp().run()