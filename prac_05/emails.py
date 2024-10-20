"""
CP1404 - Ashton Stewart
email dictionary writer
"""

#creates an initial empty dictionary
email_list = {}
#defines an initial input to start the upcoming loop
email_input = "initial"
predicted_name = ""

while email_input != "":
    #gets the email
    email_input = input("Email: ")
    if email_input != "":
        #splits the email displays the portion before the @ as a prediction of their name
        predicted_name = email_input.split("@")[0]

        #asks if the predicted portion is correct to their name. Always is lower case to fit if statement.
        name_checker = input(f"Is {predicted_name} your name? y/n ").lower()

        #ensures a name is provided
        if name_checker != "y" or "":
            predicted_name = input("What is your name? ")

            #adds the users inputted name and email
        email_list[email_input] = predicted_name


print("Provided emails and their owners:")

#displays all names and the email
for key, value in email_list.items():
    print(f"{value}: ({key})")