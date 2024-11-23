"""
CP1404 - Practical 09
Ashton Jack Stewart
Band class
"""

from musician import Musician

class Band:
    """CLass for band objects"""

    def __init__(self, name = "", year = 0, cost = 0.0):
        """Creates an object"""
        super().__init__()
        self.name = name
        self.year = year
        self.cost = cost
        self.all_musicians = []
        self.instruments = []


    def __str__(self):

        return f"stuff"

    def add(self, instrument):
         """Add an instrument to musician's collection."""
         self.instruments.append(instrument)
