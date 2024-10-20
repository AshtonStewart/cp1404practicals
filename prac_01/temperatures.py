#Provided menu that gives options.
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
#displays the menu
print(MENU)
#gets an input that should be one of the menu items.
choice = input(">>> ").upper()
#sets up a loop that can be broken at any point.
while choice != "Q":
    #converts celcius to farenheit if celcius is chosen.
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    #calculates and converts celcius to farenheit then prints it.
    elif choice == "F":
        fahrenheit = float(input("farenheit: "))
        celsius = (fahrenheit - 32) / 9.0 * 5
        print(f"Result: {celsius:.2f} F")
    else:
        #accounts for if C or F or Q isn't chosen.
        print("Invalid option")
    #repeats the menu and gets the input.
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
