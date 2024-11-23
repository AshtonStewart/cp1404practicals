"""
CP1404 - Practical 09
Ashton Jack Stewart
Silver_service_taxi test
"""

from silver_service_taxi import silverservicetaxi

hummer = silverservicetaxi("Hummer", 200, 4)
concept_car = silverservicetaxi("Overpriced car", 100, 2)

print(hummer)
hummer.start_fare()
hummer.drive(20)
print(f"The fare is: ${hummer.get_fare()}")

print(concept_car)
concept_car.start_fare()
concept_car.drive(18)
print(f"The fare is: ${concept_car.get_fare()}")
