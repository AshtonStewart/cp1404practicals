"""
Ashton Jack Stewart
Practical 06 - programming_languages
started: 2:46pm
Finished: 11:28am
"""

class Guitar:
    def __init__(self, name = "", year = 0, cost = 0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return(f"{self.name} ({self.year}) : ${self.cost}")

    def __get_age__(self):
        return(self.year)
    def __is_vintage__(self):
        #vintage = [guitar.name for guitar in guitars if (2024 - guitar.year) > 50]
        print("temporary crash stopper")