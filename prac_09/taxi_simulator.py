"""
CP1404 Practical- 09
Ashton Jack Stewart
Taxi simulator
"""


from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def main():
    """Sets an initial set of values for the class and functions to use"""
    print("Lets drive!")
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    menu = "q)uit, c)hoose taxi, d)rive"
    current_taxi = "not chosen"
    choice = ""
    bill_to_date = 0

    choose_action(taxis, menu, current_taxi, choice, bill_to_date)

def choose_action(taxis, menu, current_taxi, choice, bill_to_date):
    """Gives the user a set of choices"""
    while choice != "q":
        choice = input(f"Please choose from the menu: \n{menu} \n>>>").lower()
        if choice == "c":
            current_taxi = choose(taxis)
        elif choice == "d":
            drive(current_taxi)
            print("d")
        elif choice != "q":
            print("Invalid selection")
        print(f"bill to date: ${bill_to_date}")

def choose(taxis):
    """Displays a list of taxis and their data for the user to choose from"""
    taxi_num = 0
    int_check = False
    for taxi in taxis:
        print(f"{taxi_num} - {taxi}")
        taxi_num += 1
    while int_check == False:
        try:
            chosen_taxi = int(input("Choose taxi: "))
            int_check = True
        except ValueError:
            print("Invalid input")

def drive(current_taxi):
    if current_taxi == "not chosen":
        print("You must choose a taxi first")
    else:
        print("")

if __name__ == "__main__":
    main()