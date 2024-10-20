"""
CP1404 - Practical 3
Ashton Jack Stewart
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished: #creates a loop that keeps going as long as a non integer is given
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True #breaks the loop when an integer is given
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)