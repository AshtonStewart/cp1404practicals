"""
Ashton Jack Stewart
Practical 07 - guitar
"""

#Global variable:
current_year = 2024
vintage_age = 50


class Guitar:
    def __init__(self, name = "", year = 0, cost = 0):
        """Initialist a guitar instance.
            name = text
            year = int
            cost = float (1:1) for dollars"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """This function prints details of the guitar"""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def calc_age(self):
        """This function calculates the age of the guitar"""
        return current_year - self.year

    def is_vintage(self):
        """This function returns True if the guitar is over 50 years old"""
        return self.calc_age() >= vintage_age

    def __lt__(self, other):
        """This function sorts and returns the ages of the guitars based on which are higher than others"""
        return self.year < other.year
