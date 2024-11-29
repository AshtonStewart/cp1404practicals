"""cp1404 Ashton Stewart
Program to get a password from the user that generates a star per character
"""
#main function
def main():
    min_pass_length = 6
    password = get_password(min_pass_length)

def get_password(min_pass_length):
    userpass = input("What is your password? ")
    while len(userpass) < min_pass_length:
        print(f"Your password must be at least {min_pass_length} characters long.")
        userpass = input("What is your password? ")

    starprinter(len(userpass))

def starprinter(starlength):
    print("*" * starlength)

main()

print("Process concluded")