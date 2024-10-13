"""
CP1404 - Practical 4
Ashton Jack Stewart

"""

def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_of_months = int(input("How many months? ")) #this variable stores the number of months as a scalar value

    for month in range(1, num_of_months + 1):
        #income = float(input("Enter income for month " + str(month) + ": "))
        income = float(input(f"Enter income for month {month}: $"))
        incomes.append(income)

    print_report(num_of_months, incomes)

def print_report(num_of_months, incomes): #defines function and also states it needs and therefore is dependent on inputs of
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, num_of_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))

main()


#Think about how to do this before reading on...

#We need a list to store the incomes.
#How do you add values to a list?
# list.append(input)

#We need a counter variable (int) for the month number.
#Remember that list indexes start at 0, but we want to print from 1.
#
#How many loops will we need? What kind of loops?
# 3. 1 for asking incomes, 1 for printing each months income and 1 for printing cumulative incomes

#We need a cumulative total to update as we loop through the list to display the incomes.
#
#And lastly we need to format the output nicely, which we can use f-strings for.