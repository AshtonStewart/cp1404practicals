#creates a loop that goes forever
while True:

    #gets the value of their sales. (could also be an int input)
    sales = float(input("Enter sales: $"))

    #checks if sales are equal to, or greater than 1k.
    if sales >= 1000:
        print(f"{sales * 0.15} is the bonus")

    #works for other cases. This could also be replaced with "elif sales < 1000" but this is less efficient
    else:
        print(f"{sales * 0.1} is the bonus")
