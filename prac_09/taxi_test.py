"""
CP1404 - practical 09
Ashton Jack Stewart
Taxi_test
"""

from taxi import Taxi

my_taxi = Taxi("Prius 1", 100)

my_taxi.drive(40)
print(f"Taxi details: {my_taxi}, fare: {my_taxi.get_fare()}")
# Resets the fare
my_taxi.start_fare()
my_taxi.drive(100)
print(f"Taxi details: {my_taxi}, fare: {my_taxi.get_fare()}")
