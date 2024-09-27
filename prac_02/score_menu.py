"""cp1404 Ashton Stewart
Menu system that gets a score and does stuff.
"""

def main():
    MENU = """
        H - Give score (must be between 0 and 100)
        P - print score result
        S - Print as many stars as the score
        Q - Quit
        """
    print(MENU)
    inp_score = None
    choice = input(">>> ").upper()

    while choice == "P" or choice == "S" and inp_score is None:
        print("You must give an H value first")
        print(MENU)
        choice = input(">>> ").upper()
    else:

        while choice != "Q":
            if choice == "H":
                inp_score = int(input("What is your score? "))
                while inp_score < 0 or inp_score > 100:
                    inp_score = int(input("Your score must be between 0 and 100 "))

            elif choice == "P":
                print("Your score is " + score_categorizer(inp_score))

            elif choice == "S":
                print(starprint(inp_score))

            else:
                print("Invalid selection")
            print(MENU)
            choice = input(">>> ").upper()

    print("Process concluded")

def starprint(length):
    return"*" * length

def score_categorizer(inp_score):
    if inp_score > 100 or inp_score < 0:
        return "invalid"
    elif inp_score >= 90:
        return "excellent"
    elif inp_score >= 50:
        return "good"
    else:
        return "bad"

main()