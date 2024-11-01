"""

"""

from guitar import Guitar

def input_guitar_info():
    guitar_nest = []
    guitar_name = "Not nothing!"
    info_loop = True
    while info_loop == True:
        int_guitar_year_check = False
        int_guitar_cost_check = False
        guitar_info = []

        name = input("What's the guitars name? ")

        if name != "":
            guitar_info.append(name)
            #gets the age as an integer and nothing else
            while int_guitar_year_check is False:
                try:
                    year = int(input("When was the guitar made?: "))
                    int_guitar_year_check = True
                except ValueError:
                    print("This is not a number. Please give a number")
            guitar_info.append(year)

            #gets the cost as an integer and nothing else
            while int_guitar_cost_check is False:
                try:
                    value = int(input("What's the guitars value?: "))
                    int_guitar_cost_check = True
                except ValueError:
                    print("This is not a number. Please give a number")
            guitar_info.append(value)

            #adds the new guitar info to the nest
            guitar_nest.append(guitar_info)
        else:
            info_loop = False


    print("These are my guitars;")
    count = 0
    for each_guitar in guitar_nest:
        count += 1
        print(f" Guitar.{count}:    {each_guitar[0]}, ({each_guitar[1]}), worth ${each_guitar[2]}")


input_guitar_info()