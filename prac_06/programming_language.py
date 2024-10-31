"""2:46"""



class programminglanguage:
    def __init__(self, name = "", typed = "", reflect = False, year = 0):
        self.name = name
        self.typed = typed
        self.reflect = reflect
        self.year = year
        print(self)


    def is_dynamic(self):
        print(self)


    def __str__(self):
        print(self)