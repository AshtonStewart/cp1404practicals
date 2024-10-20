"""
CP1404 - Practical 3
Ashton Jack Stewart
Password checker "skeleton" code to help you get started
"""

#original given code
MIN_LENGTH = 2
MAX_LENGTH = 6
IS_SPECIAL_CHARACTER_REQUIRED = True #changes btween True and False to run code
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""

    #new code
    #checks if password is the correct amount of characters
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    #sets counts to 0
    number_of_lower = 0
    number_of_upper = 0
    number_of_digit = 0
    number_of_special = 0

    #Loops through the password and checks each character
    for character in password:
        if character.islower():
            number_of_lower += 1
        elif character.isupper():
            number_of_upper += 1
        elif character.isdigit():
            number_of_digit += 1
        else:
            number_of_special += 1
        pass
    #checks if minimum of specific character types are met
    if number_of_lower == 0 or number_of_upper == 0 or number_of_digit == 0:
        return False
    #checks if special characters are given only when required
    elif number_of_special == 0 and IS_SPECIAL_CHARACTER_REQUIRED:
        return False
    #returns true if all parameters are met
    else:
        return True

main()