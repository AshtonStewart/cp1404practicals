"""2:46"""



class Programminglanguage:
    def __init__(self, name = "", typed = "", reflect = False, year = 0):
        self.name = name
        self.typed = typed
        self.reflect = reflect
        self.year = year
        print(self)


    def is_dynamic(self):
        print(self)

    def __str__(self):
        return (f"{self.name}, Dynamic typing = {self.typed}, Reflection = {self.reflect}, First appeared = {self.year}")