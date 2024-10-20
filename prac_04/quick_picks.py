"""
CP1404 - Practical 4
Ashton Jack Stewart
random sorted number row generator
"""

import random

quick_picks_quantity = int(input("How many quick picks as a number?: ")) #gets the amount of rows
nest_of_rows = []
for quick_pick in range(quick_picks_quantity): #makes loop based on size of user input
    new_row = [] #resets new_row to prepare it for next set of values
    i = 0 #resets i for next loop
    for i in range(6):
        random_number = random.randint(1, 45) #generates random number between 1 and 45
        while random_number in nest_of_rows: #checks if new random number is in list, if so loops through until it;
            random_number = random.randint(1, 45) #generates a random number between 1 and 45 that's not in the list
        new_row.append(random_number) #adds new number to list
        new_row = sorted(new_row) #arranges the row in ascending order

    nest_of_rows.append(new_row) #nests new row in list

for n in nest_of_rows: #loops through list of rows
    print(" ".join("{:3}".format(row) for row in n))#prints row without '[' or ']' and formats numbers to be aligned

