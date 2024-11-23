"""
CP1404 - Practical 09
Ashton Jack Stewart
Silver_service_taxi test
"""

from silver_service_taxi import silverservicetaxi

hummer = silverservicetaxi("Hummer", 200, 4)

print(hummer)
hummer.start_fare()
hummer.drive(20)
print(hummer.get_fare())