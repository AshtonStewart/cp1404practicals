"""
CP1404 - Practical 08
Dyanmic Labels
Ashton Stewart
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

class DynamicLayoutApp(App):

    def __init__(self, **kwargs):
        '''Defines a generic bunch of names'''
        super().__init__(**kwargs)
        self.names = ["Ashton, Bok, Bringus, Brongus, Bingus, Bongus"]

    def build(self):
        '''Builds the UI'''
        self.title = "Dynamic demo"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.new_widgets()
        return self.root

    def new_widgets(self):
        print("Begone empty function warning")
        for name in self.names:
            return self.root.add_widget(Button(text=name))

DynamicLayoutApp().run()