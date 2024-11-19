"""
CP1404 - Practical 08: Box Layout Demo
Ashton Stewart
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """Builds GUI"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        '''Changes text in the Greeting box to the given name'''
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Clears all text from the output_label box"""
        self.root.ids.output_label.text = ""


BoxLayoutDemo().run()
