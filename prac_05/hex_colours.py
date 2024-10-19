"""
CP1404 - Ashton Stewart
hex colours in a dictionary
"""

hex_colour_codes = {"absolutezero": "#0048ba",
                    "aqua": "#00ffff",
                    "babyblue": "#89cff0",
                    "bisque1": "#ffe4c4",
                    "bleudefrance": "#318ce7",
                    "brightgreen": "#66ff00",
                    "chestnut": "#954535",
                    "cinereous": "#98817b",
                    "cornflowerblue": "#6495ed"}

#gets the colour from the user, then turns all letters to lower case then removes all spaces
#this also means if the user inputs "  " it will end the loop
chosen_colour = input("What colour code do you want? ").lower().replace(" ", "")

#keeps asking for inputs as long as the user does not enter ""
while chosen_colour != "":

    #if the person gives a valid name:
    try:
        output_code = hex_colour_codes[chosen_colour] #chooses hex colour associated with colour name
        print(f"The code for {chosen_colour} is {output_code}") #prints all the info

        #gets the new colour name from the user, then turns all letters to lower case then removes all spaces
        chosen_colour = input("What colour code do you want? ").lower().replace(" ", "")

    #error checks then continues the code
    except:
        print("Invalid name, please choose another")

        #gets the colour from the user, then turns all letters to lower case then removes all spaces
        chosen_colour = input("What colour code do you want? ").lower().replace(" ", "")

print("Colour picking concluded")