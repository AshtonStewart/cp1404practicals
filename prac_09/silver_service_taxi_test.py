"""
CP1404 - Practical 09
Ashton Jack Stewart
Silver_service_taxi test
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    """Shows a before and after of each car driving a distance and the fare for that drive."""
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    concept_car = SilverServiceTaxi("Overpriced car", 100, 2)
    print(hummer)
    hummer.start_fare()
    hummer.drive(20)
    print(hummer)
    print(f"The fare is: ${hummer.get_fare()}")

    print(concept_car)
    concept_car.start_fare()
    concept_car.drive(18)
    print(concept_car)
    print(f"The fare is: ${concept_car.get_fare()}")

main()
