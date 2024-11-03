"""
Ashton Jack Stewart
Practical 06 - guitars
Guessed time: About an hour
Actual time: About an hour
"""

from guitar import Guitar

def main():
    """Code to further demonstrate functionality of class in guitar.py"""

    all_guitars = []
    guitar_name = "Not nothing!"


    info_loop = True
    while info_loop == True:
        int_guitar_year_check = False
        int_guitar_cost_check = False
        guitar_info = []

        name = input("What's the guitars name? ")

        if name != "":
            #gets the age as an integer and nothing else
            while int_guitar_year_check is False:
                try:
                    year = int(input("When was the guitar made?: "))
                    int_guitar_year_check = True
                except ValueError:
                    print("This is not a number. Please give a number")

            #gets the cost as an integer and nothing else
            while int_guitar_cost_check is False:
                try:
                    value = float(input("What's the guitars value?: "))
                    int_guitar_cost_check = True
                except ValueError:
                    print("This is not a number. Please give a number")
            #adds the new guitar info to the nest


            all_guitars.append(Guitar(name, year, value))
        else:
            info_loop = False

    #all_guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    #all_guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("These are my guitars;")
    count = 0
    for each_guitar in all_guitars:
        count += 1
        if each_guitar.is_vintage() == True:
            is_vintage = "(Vintage)"
        else:
            is_vintage = ""
        print(f"Guitar {count}: {each_guitar.name:>20} ({each_guitar.year}), worth ${each_guitar.cost:10,.2f} {is_vintage}")


main()