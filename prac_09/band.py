"""
CP1404 - Practical 09
Ashton Jack Stewart
Band class
"""

from musician import Musician

class Band:
    """Class for band objects"""

    def __init__(self, name = ""):
        """Creates an object"""
        super().__init__()
        self.name = name
        self.musicians = []

    def __str__(self):
        """Formats a string of musicians"""
        self.all_musicians = ', '.join(str(musician) for musician in self.musicians)
        return f"{self.name} ({self.all_musicians})"

    def add(self, musician):
        """Add a player to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the instrument playing their first (or no) instrument."""
        return '\n'.join([musician.play() for musician in self.musicians])