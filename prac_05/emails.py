"""
CP1404 - Ashton Stewart
email dictionary writer
"""

email_list = {}

email_input = "initial"
predicted_name = ""

while email_input != "":
    email_input = input("What's your email?")
    name_checker = input(f"is {predicted_name} your name? y/n ")

    if name_checker == "y" or name_checker == "":
        email_list[email_input] = predicted_name

    print(email_list)

print("Creation of dictionary finished")