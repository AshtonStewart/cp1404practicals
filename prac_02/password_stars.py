

def passtostars(userpass):
    min_pass_length = 3
    #user_password = input("What is your password?")
    if len(userpass) < min_pass_length:
        print(f"Your password must be at least {min_pass_length} characters long.")
    else:
        print("*" * len(userpass))

passtostars("0924h5g4")