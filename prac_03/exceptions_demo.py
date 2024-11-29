"""
CP1404 - Practical 3
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0: #checks if the denominator is 0 and endlessly loops till it is not 0.
        denominator = int(input("Denominator can't be 0. Enter a new denominator: ")) #gets the new denominator

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")

#Q: When will a ValueError occur?
#A: When an invalid numerator or denominator is given. This includes non integers or imaginary numbers

#Q: When will a ZeroDivisionError occur?
#A: When the user inputs the denominator to be 0

#Q: Can you change the code to avoid the possibility of a ZeroDivisonError?
#A: Yes. While you cannot ever divide by zero, you can have extra code that forces the input to not be 0.