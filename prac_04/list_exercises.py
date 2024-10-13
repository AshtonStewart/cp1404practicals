"""
CP1404 - Practical 4
Ashton Jack Stewart
Relay and organise user inputs
+
security checker
"""

#number sorter

numbers = []
print("please give 5 values")
for i in range(0, 5, 1): #loops through values 0, 1, 2, 3, 4
    numbers.append(int(input(f"Input number {i + 1} : "))) #gets a user input which is added to the end of the list

for i in range(0, 5, 1): #loops through values 0, 1, 2, 3, 4
    print(f"number {i + 1}: {numbers[i]}") #prints the number values in order

first_number = numbers[0] #gets the first number
print(f"The first number is: {first_number}")
last_number = numbers[-1] #gets the last number
print(f"The last number is: {last_number}")
smallest_number = min(numbers) #gets the smallest
print(f"The smallest number is: {smallest_number}")
largest_number = max(numbers) #gets the largest number
print(f"The largest number is: {largest_number}")
average_of_numbers = sum(numbers) / len(numbers) #gets the sum of numbers then divides it by how many numbers are in the list
print(f"The average of the numbers is: {average_of_numbers}")

#username checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username_input = input("please type your username: ")
username_matches = 0

for username in usernames: #loops through usernames
    if username == username_input: #checks if the input matches the current iteration of the loop
        username_matches = 1 #changes a value that can be used for checking later

if username_matches == 1: #uses the value from before to see if there was a match and responds accordingly
    print("Access granted")
else:
    print("Access denied")
