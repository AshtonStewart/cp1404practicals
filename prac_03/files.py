"""
CP1404 - Practical 3
Ashton Jack Stewart
different ways to open, look at, and edit files
"""

#Code 1:

file_one_name = "name.txt"
name = input("What is your name? ")  #gets the name
file_one_output = open(file_one_name, 'w')   #opens the file to write
print(name, file=file_one_output, end='')#writes the name to the files without adding extra lines
file_one_output.close()                  #closes the file

#Code 2:
file_one_read = open(file_one_name, 'r')
name_in_file = file_one_read.read()
print(f"Hi {name_in_file}!")
file_one_read.close()                #closes the file


#Code 3:
txt_numbers = []
file_two_name = "numbers.txt"
with open(file_two_name, 'r') as file_two:
    for line in file_two:
        txt_numbers.append(int(line))
    first_two_lines_sum = txt_numbers[0] + txt_numbers[1]
    print(f"Sum of first two lines: {first_two_lines_sum}")
    all_lines_sum = sum(txt_numbers)
    print(f"Sum of all lines: {all_lines_sum}")
