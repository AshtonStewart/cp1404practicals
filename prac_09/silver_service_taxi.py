"""
CP1404 - Practical 09
Ashton Jack Stewart
Silver_service_taxi class
"""


from taxi import Taxi

class silverservicetaxi(Taxi):
    """Represents a fancy taxi object"""

    def __init__(self, name, fuel):
        super().__init__(name, fuel)
        self.fancy_fare_multi = 2.5


    def __str__(self):
        return f"{super().__str__()}"
