"""
CP1404 - Practical 09
Ashton Jack Stewart
Silver_service_taxi class
"""


from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Represents a fancy taxi object"""

    def __init__(self, name, fuel, fanciness):
        """Constructs an object"""
        super().__init__(name, fuel)
        self.flagfall = 4.50
        self.price_per_km *= fanciness


    def __str__(self):
        """Returns a string representation of the taxi"""
        return f"{super().__str__()} Plus flagfall of ${self.flagfall}"

    def get_fare(self):
        """Return the price for the taxi trip (inclduing the additional costs for fanciness and flagfall)"""

        return super().get_fare() + self.flagfall
        #return (self.price_per_km * self.current_fare * self.fancy_fare_multi) + self.flagfall

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare = 0

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = distance
        self.current_fare += distance_driven
        return distance_driven

