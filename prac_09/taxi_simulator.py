"""
CP1404 Practical- 09
Ashton Jack Stewart
Taxi simulator
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def main():
    """Sets an initial set of values for the class and functions to use then gives the user a list of choices"""
    print("Lets drive!")
    TAXIS = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    MENU = "q)uit, c)hoose taxi, d)rive"
    current_taxi = None
    choice = None
    bill_to_date = 0

    while choice != "q":
        choice = input(f"Please choose from the menu: \n{MENU} \n>>>").lower()
        if choice == "c":
            current_taxi = choose(TAXIS)
            print(f"bill to date: ${bill_to_date}")
        elif choice == "d":
            bill_to_date += drive(current_taxi, TAXIS)
            print(f"bill to date: ${bill_to_date}")
        elif choice != "q":
            print("Invalid selection")
            print(f"bill to date: ${bill_to_date}")
    print(f"Final bill: ${bill_to_date}")
    display_taxis(TAXIS)

def choose(taxis):
    """Displays a list of taxis and their data for the user to choose from"""
    chosen_taxi = -1
    error_check = False
    display_taxis(taxis)

    #error checking
    while error_check == False:
        try:
            chosen_taxi = int(input("Choose taxi: "))
            if chosen_taxi not in range(len(taxis)):
                print("invalid taxi")
            else:
                error_check = True
        except ValueError:
            print("Invalid input")
    return chosen_taxi

def drive(current_taxi, taxis):
    """Drives the taxi based off a given distance"""
    error_check = False

    #error checking
    if current_taxi == None:
        print("You must choose a taxi first")
    else:
        while error_check == False:
            try:
                distance_input = int(input("Drive how far? "))
                if distance_input < 0:
                    print("invalid distance")
                else:
                    error_check = True
            except ValueError:
                print("Invalid input")


        taxis[current_taxi].start_fare()
        taxis[current_taxi].drive(distance_input)
        bill_for_ride = taxis[current_taxi].get_fare()
        bill_for_ride = round(bill_for_ride, 2)
        print(f"Fare for that taxi ride was: ${bill_for_ride}")
        return bill_for_ride

def display_taxis(taxis):
    """Displays a list of taxis"""
    taxi_num = 0
    for taxi in taxis:
        print(f"{taxi_num} - {taxi}")
        taxi_num += 1

if __name__ == "__main__":
    main()