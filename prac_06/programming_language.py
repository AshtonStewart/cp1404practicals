"""
Ashton Jack Stewart
Practical 06 - programming_languages
started: 2:46pm
Finished: 11:28am
"""

class Programminglanguage:
    def __init__(self, name, typed, reflect = False, year = 0):
        """Creates initial instances. """

        self.name = name
        self.typed = typed
        self.reflect = reflect
        self.year = year
        print(self)

    def __str__(self):
        """returns text using the instance values"""
        return (f"{self.name}, typing = {self.typed}, Reflection = {self.reflect}, First appeared = {self.year}")

    def is_dynamic(self):
        """checks if the instance is dynamic"""
        return self.typed.lower() == "dynamic"