"""
CP1404/CP5632 - Practical
Ashton Jack Stewart
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True #breaks the loop when an integer is given
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)