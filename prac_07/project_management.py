"""
Ashton Jack Stewart
Project data saving and modification
"""

menu = ("- (L)oad projects  \n"
        "- (S)ave projects)  \n"
        "- (D)isplay projects  \n"
        "- (F)ilter projects by date \n"
        "- (A)dd new project  \n"
        "- (U)pdate project \n"
        "- (Q)uit")

def main():
    chosen_action = "Not nothing"
    while chosen_action != "Q":
        print(menu)
        chosen_action = input(">> ").upper()

        if chosen_action == "L":
            print("Load")

        elif chosen_action == "S":
            print("save")

        elif chosen_action == "D":
            print("Display")

        elif chosen_action == "F":
            print("Filter by date")

        elif chosen_action != "Q":
            print("Invalid menu choice")

main()