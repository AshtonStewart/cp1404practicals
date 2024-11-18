"""
CP1404 - practical 7
Ashton Jack Stewart
"""

from guitar import Guitar

import csv
file_name = "guitars.csv"
def main():
    #Gets details of the file and puts them into a list which is added onto with user inputs then exported to excel

    all_guitar_info = []


    #gets the guitars from the csv and stores them in a nest.
    with open(file_name, "r") as in_file:
        reader = csv.reader(in_file)
        for line in reader:
            all_guitar_info.append(Guitar(line[0], int(line[1]), float(line[2])))


    #gets the users inputs then adds them to that nest
    info_loop = True
    while info_loop == True:
        year_is_int = False
        cost_is_bool = False
        guitar_info = []

        name = input("What's the guitars name? ")

        if name != "":
            # gets the age as an integer and nothing else
            while year_is_int is False:
                try:
                    year = int(input("What year was the guitar made?: "))
                    year_is_int = True
                except ValueError:
                    print("This is not real year. Please give a valid year")

            # gets the cost as an integer and nothing else
            while cost_is_bool is False:
                try:
                    cost = float(input("What's the guitars value?: "))
                    cost_is_bool = True
                except ValueError:
                    print("This is not a valid cost. Please give a valid cost")
            # adds the new guitar info to the nest

            all_guitar_info.append(Guitar(name, year, cost))
        else:
            info_loop = False


    #sorts all guitars
    all_guitar_info.sort()

    #prints all guitars from the nest
    print("These are my guitars;")
    count = 0
    for each_guitar in all_guitar_info:
        count += 1
        if each_guitar.is_vintage() == True:
            is_vintage = "(Vintage)"
        else:
            is_vintage = ""
        print(
            f"Guitar {count}: {each_guitar.name:>20} ({each_guitar.year}), worth ${each_guitar.cost:10,.2f} {is_vintage}")


    #exports the data to the csv file
    with open(file_name, "w", newline='') as out_file:
        writer = csv.writer(out_file)

        for new_line in all_guitar_info:
            writer.writerow([new_line.name, new_line.year, new_line.cost])

main()