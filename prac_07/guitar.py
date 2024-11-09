"""
Ashton Jack Stewart
Practical 07 - guitar
"""

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
        """prints details of the guitar"""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """gets the age of the guitar"""
        current_year = 2024
        return_year = current_year - self.year
        return return_year

    def is_vintage(self):
        """Returns True if the guitar is over 50 years old"""
        vintage_age = 50
        return self.get_age() >= vintage_age

    def __lt__(self, other):
        """returns the ages based on which are higher than others"""
        return self.year > other.year
