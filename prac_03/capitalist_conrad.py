"""
CP1404 - Practical 3
Ashton Jack Stewart
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random


FILE_NAME = "capitalist_conrad_output.txt"
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
number_of_days = 0 #gives the initial amount of days
price = INITIAL_PRICE #sets the price to be the intial price
out_file = open(FILE_NAME, 'w') #opens the file for writing

while MIN_PRICE <= price <= MAX_PRICE:

        daily_output = f"On day {number_of_days} the price is ${price:,.2f}" #states what the day and price is
        price_change = 0
        # generate a random integer of 1 or 2
        # if it's 1, the price increases, otherwise it decreases
        if random.randint(1, 2) == 1:
            # generate a random floating-point number
            # between 0 and MAX_INCREASE
            price_change = random.uniform(0, MAX_INCREASE)
        else:
            # generate a random floating-point number
            # between negative MAX_DECREASE and 0
            price_change = random.uniform(-MAX_DECREASE, 0)

        price *= (1 + price_change) #increases the price
        print(daily_output) #prints the previously determined daily output
        number_of_days += 1 #increases the days by 1
        print(daily_output, file=out_file)  # write to file

out_file.close() #closes the file