"""
CP1404 - Practical 08
Dyanmic Labels
Ashton Stewart
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label

class DynamicLayoutApp(App):

    def __init__(self, **kwargs):
        """Defines a generic bunch of names"""
        super().__init__(**kwargs)
        self.names = ["Ashton", "Bok", "Bringus", "Brongus", "Bingus", "Bongus", "Cam"]

    def build(self):
        """Builds the UI"""
        self.title = "Dynamic demo"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.new_widgets()
        return self.root

    def new_widgets(self):
        """Creates a new widget for all the given names"""
        for name in self.names:
            self.root.add_widget(Label(text=name))

DynamicLayoutApp().run()