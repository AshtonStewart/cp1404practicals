"""
CP1404 - practical 7
Ashton Jack Stewart
"""

from guitar import Guitar

import csv
file_name = "guitars.csv"
def main():

    all_guitar_info = []

    with open(file_name, "r") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        for line in reader:
            all_guitar_info.append(Guitar(line[0], int(line[1]), float(line[2])))

    info_loop = True
    while info_loop == True:
        int_guitar_year_check = False
        int_guitar_cost_check = False
        guitar_info = []

        name = input("What's the guitars name? ")

        if name != "":
            # gets the age as an integer and nothing else
            while int_guitar_year_check is False:
                try:
                    year = int(input("When was the guitar made?: "))
                    int_guitar_year_check = True
                except ValueError:
                    print("This is not a number. Please give a number")

            # gets the cost as an integer and nothing else
            while int_guitar_cost_check is False:
                try:
                    value = float(input("What's the guitars value?: "))
                    int_guitar_cost_check = True
                except ValueError:
                    print("This is not a number. Please give a number")
            # adds the new guitar info to the nest

            all_guitar_info.append(Guitar(name, year, value))
        else:
            info_loop = False


    #sorts all guitars
    all_guitar_info.sort()

    #prints all guitars in order of age
    for i in range(len(all_guitar_info)):
        print(all_guitar_info[i])




    with open(file_name, "w", newline='') as out_file:
        writer = csv.writer(out_file)
        for new_line in all_guitar_info:
            writer.writerow([new_line.name, new_line.year, new_line.value])

main()