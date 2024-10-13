"""
CP1404 - Practical 4
Ashton Jack Stewart
Relay and organise user inputs
+
security checker
"""

numbers = []
print("please give 5 values")
for i in range(0, 5, 1):
    numbers.append(int(input(f"Input number {i} : ")))

for i in range(0, 5, 1):
    print(f"number {i + 1}: {numbers[i]}")

first_number = numbers[0]
print(f"The first number is: {first_number}")
last_number = numbers[-1]
print(f"The last number is: {last_number}")
smallest_number = min(numbers)
print(f"The smallest number is: {smallest_number}")
largest_number = max(numbers)
print(f"The largest number is: {largest_number}")
average_of_numbers = sum(numbers) / len(numbers)
print(f"The average of the numbers is: {average_of_numbers}")


