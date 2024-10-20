"""
CP1404 - Practical 3
Ashton Jack Stewart
Examples of using python string formatting in printing.
"""
import math #imports math for later rounding
name = "Gibson L-5 CES"
year = 1922
cost = 16035.9

# The 'old' manual way to format text with string concatenation (don't do this):
print("My guitar: " + name + ", first made in " + str(year))

# A better way - using str.format() (don't do this unless you need to):
print("My guitar: {}, first made in {}".format(name, year))
print("My guitar: {0}, first made in {1}".format(name, year))
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))

# And with f-string formatting, introduced in Python 3.6 (do this)
print(f"My {name} was first made in {year} (that's right, {year}!)")

# Formatting currency (grouping with comma, 2 decimal places):
print("My {} would cost ${:,.2f}".format(name, cost))  # str.format version
print(f"My {name} would cost ${cost:,.2f}")  # preferred f-string version

# Aligning columns by using width after the :
# This loop uses enumerate, which is useful when you want both the index and value
numbers = [1, 19, 123, 456, -25]

for i, number in enumerate(numbers, 1):
    print(f"Number {i} is {number:5}")


cost = math.ceil(cost) #rounds up from 16035.90 to 16036
print(f"{year} {name} for about ${cost}") #prints the rounded year, name, and rounded cost of guitar

for current_power_value in range(0, 11, 1): #creates a range / loop for 10 values.
    #prints 2^x with 10 increasing x values. All of which are aligned in requested format
    print(f"2^{current_power_value:2} is {2 ** current_power_value:4}")
