"""
cp1404 - Ashton Jack Stewart
Processing csv files using nests and dictionaries
"""


champions_and_wins_total = {}
thing = []

import csv
#Champion and how many times they've won
def main():
    with open('wimbledon.csv', "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)

        c_and_ws = champion_scorer()
        first_row_excluder = 0
        for row in reader:
            if first_row_excluder != 0:
                champions_and_wins_total[row[2]] = row[5]


            first_row_excluder += 1
    #print(thing)

def country_name_sorter():
    print("bok")

def champion_scorer():
    #score = row[5].split(":")[0]
    #print(f"bok {score}")
    print("bok")

def info_printer():
    print("bok")

#need to finish


#for champion, total_wins in champions_and_wins_total.items():
   #print(f"{champion}: {total_wins}")


#print(champions_and_wins_total)
#counties of the champions in alphabetical order