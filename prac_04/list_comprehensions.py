"""
CP1404 - Practical 4
Ashton Jack Stewart
list comprehensions and ways to edit lists
"""

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

# for loop that creates a new list containing the first letter of each name
first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)

# list comprehension that does the same thing as the loop above
first_initials = [name[0] for name in names]
print(first_initials)

# list comprehension that creates a list containing the initials
# this splits each name and adds the first letters of each part to a string
full_initials = [name.split()[0][0] + name.split()[1][0] for name in full_names]
print(full_initials)

# this example uses filtering to select only the names that start with A
a_names = [name for name in names if name.startswith('A')]
print(a_names)

# and here's the join string method being used to create a single string from the names like:
# 'Ada Alan Angel Bob Jimi'
print(" ".join(sorted(names)))

#Code 1: convert string of both capital and lowercase letters to only lowercase.
lower_case_full_name = []
for name in full_names: #loops through names
    lower_case_full_name.append(name.lower()) #makes name lower case
print(lower_case_full_name) #prints new list

#Code 2: convert string of text to list of numbers
almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
real_numbers = []
for fake_number in almost_numbers: #loops through string
    real_numbers.append(int(fake_number)) #adds the text as a number to the end of the list
print(real_numbers)

#Code 3: creates a list with only numbers greater than 9 in 'real_numbers' from Code 2
greater_than_nine = []
for number_to_check in real_numbers: #loops through numbers
    if number_to_check > 9: #checks if number is greater than 9
        greater_than_nine.append(number_to_check) #adds the number if it is
print(greater_than_nine)

#Code 4: prints last names of full names with more than 11 characters
longer_than_eleven = []
pos = 0 #gets a position
for name_to_check in full_names: #loops through all names

    name_length = len(name_to_check) #gets the length of characters in the name
    if name_length > 11: #checks if the name is longer than 11 characters

        #takes valid last name and slices off first name
        last_name_to_be_added = full_names[pos].split()[1]
        #adds result from previous line to list
        longer_than_eleven.append(last_name_to_be_added)
    pos += 1 #increases position by 1
print(longer_than_eleven)