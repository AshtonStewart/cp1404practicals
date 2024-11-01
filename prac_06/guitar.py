"""
Ashton Jack Stewart
Practical 06 - guitar
started: 12am
Finished: 1:30pm
"""

class Guitar:
    def __init__(self, name = "", year = 0, cost = 0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        return 2024 - self.year

    def is_vintage(self):
        return True if self.get_age() > 50 else False