"""
CP1404 - Practical 4
Ashton Jack Stewart
Simple list editing
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

#Without running the code, what will be the answers to the following Questions:
#Q:numbers[0]
#A:3

#Q:numbers[-1]
#A:2

#Q:numbers[3]
#A:4

#Q:numbers[:-1]
#A: [3, 1, 4, 1, 5, 9]

#Q:numbers[3:4]
#A: [1]

#Q:5 in numbers
#A:True

#Q:7 in numbers
#A:False

#Q:"3" in numbers
#A:False

#Q:numbers + [6, 5, 3]
#A: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]


#Note: Numbers is redefined before every statement/ code to reset changes made in previous code.
#Change the first element of numbers to "ten"
print(f"numbers before changes: {numbers}")
numbers[0] = "ten" #Changes the first element of numbers to "ten"
print(f"numbers after first element is changed to 'ten': {numbers}")

#change the last element to the number 1
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers[-1] = 1 #changes the last element to the number 1
print(f"numbers after last element is changed to -1: {numbers}")

#print all elements except the first two
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers = numbers[slice(2, None)]
print(f"numbers without first 2 is: {numbers}")

#print wehether 9 is an element or not
numbers = [3, 1, 4, 1, 5, 9, 2]
if 9 in numbers: #checks if 9 is in the numbers list / string
    print(f"9 is in: {numbers}") #prints if it is
else:
    print(f"9 is not in: {numbers}") #prints if it isn't