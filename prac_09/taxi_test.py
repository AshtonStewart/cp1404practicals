"""
CP1404 - practical 09
Ashton Jack Stewart
Taxi_test
"""

from taxi import Taxi

MY_TAXI = Taxi("Prius 1", 100)
def main(my_taxi):
    """Drives the taxi different distances and prints the results"""
    my_taxi.drive(40)
    print(f"Taxi details: {my_taxi}, fare: {my_taxi.get_fare()}")
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(f"Taxi details: {my_taxi}, fare: {my_taxi.get_fare()}")

main(MY_TAXI)
