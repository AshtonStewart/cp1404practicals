"""
Ashton Jack Stewart
CP1404 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    #makes limo stuff
    limo = Car(100)
    limo.add_fuel(20)
    print(f"Limo has fuel: {limo.fuel}")
    limo.drive(115)

    #testing if cars and their names can be made.
    #awesome_car = Car(200)
    #awesome_car.add_fuel(50)
    #print(f"{awesome_car.fuel}")


main()