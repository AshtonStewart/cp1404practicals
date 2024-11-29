"""
CP1404 - Ashton Stewart
hex colours in a dictionary
"""

#dictionary :O
hex_colour_codes = {"absolutezero": "#0048ba",
                    "aqua": "#00ffff",
                    "babyblue": "#89cff0",
                    "bisque1": "#ffe4c4",
                    "bleudefrance": "#318ce7",
                    "brightgreen": "#66ff00",
                    "chestnut": "#954535",
                    "cinereous": "#98817b",
                    "cornflowerblue": "#6495ed"}

#sets an initial value that starts the loop
chosen_colour = "start_the_loop!"

while chosen_colour != "":
    #gets the users input (the name of the colour)
    print("('' to quit)")
    chosen_colour = (input("What colours hex code do you want? "))

    #gets that chosen colour, removes spaces and sets everything...
    #...to be lower case so that any variation of a valid name is compatible.
    dictionary_colour_searcher = chosen_colour.lower().replace(" ", "")

    #Tries to see if the edited input works for the dictionary
    try:
        #if it does:

        # chooses hex colour associated with colour name
        output_code = hex_colour_codes[dictionary_colour_searcher]
        # prints the input and associated hex code
        print(f"The code for {chosen_colour} is {output_code}")

    #if it doesn't
    except:
        print("Invalid name, please choose another")

print("Colour picking concluded")