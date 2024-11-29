from prac_09.trees import QuickTree

#gets user name
nameinput = input("WHAT IS YOUR NAME ")

#creates and prints menu.

MENU = """H - Hello
G - Goodbye
Q - Quit
"""
print(MENU)
choice = input(">>> ").upper()

#checks what input the person sent to the menu. Sets up loop if input isn't Q
while choice != "Q":
    #says hello if choice is H
    if choice == "H":
       print("Hello", nameinput)
    #says goodbye if choice is G
    elif choice == "G":
       print("Goodbye", nameinput)
    else:
    #accounts for other stuff
        print("Invalid input")
    #reprints the menu, reminding user of options and gives chance to quit.
    print(MENU)
    choice = input(">>> ").upper()
#states that the loop has closed.
print("Process concluded")