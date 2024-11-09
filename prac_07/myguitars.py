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
            #print(f"bok {Guitar(line[0])}")
            all_guitar_info.append(Guitar(line[0], int(line[1]), float(line[2])))
    #print(all_guitar_info)
    all_guitar_info.sort()

    for i in range(len(all_guitar_info)):
        print(all_guitar_info[i])

main()