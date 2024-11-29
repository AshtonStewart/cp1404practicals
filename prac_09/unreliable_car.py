"""
CP1404 - Practial 09
Ashton Jack Stewart
Unreliable Car class
"""
import random
from car import Car

class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        """Creates an initial set of variables"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Randomly decides if the car drives the specified distance"""
        chance_to_stall = random.randint(1, 100)
        #print(Chance_to_stall)
        if chance_to_stall < self.reliability:
            distance = super().drive(distance)
        else:
             print("Car failed to start")
        return distance
