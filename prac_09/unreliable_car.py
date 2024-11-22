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

    #def drive(self, reliability):
        chance_to_drive = random.randint(1, 100)
        # if chance_to_drive > self.reliability:
        #     distance =
        # else:
        #     distance =
        # return distance
