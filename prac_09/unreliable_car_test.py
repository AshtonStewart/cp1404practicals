"""
CP1404 - Practial 09
Ashton Jack Stewart
Unreliable Car test
"""

from unreliable_car import UnreliableCar

def run_test():
    my_car = UnreliableCar("Prius 1", 100, 42)
    print(my_car)
    my_car.drive(72)
    print(my_car)

run_test()
