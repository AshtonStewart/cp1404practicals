"""
Ashton Jack Stewart
Project data saving and modification
"""
import datetime


file_name = "projects.txt"

menu = ("- (L)oad projects  \n"
        "- (S)ave projects)  \n"
        "- (D)isplay projects  \n"
        "- (F)ilter projects by date \n"
        "- (A)dd new project  \n"
        "- (U)pdate project \n"
        "- (Q)uit")

#first_line_of_file = "Name	Start Date	Priority	Cost Estimate	Completion Percentage"
first_line_of_file = ["Name",	"Start Date	Priority",	"Cost Estimate",	"Completion Percentage"]
def main():

    all_projects = info_get()
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

        elif chosen_action == "A":
            print("Add new project")
            add()

        elif chosen_action == "U":
            print("Update")

        elif chosen_action != "Q":
            print("Invalid menu choice")


def info_get():
    all_contents = []
    first_line = 0

    #opens the txt file
    with open(file_name, "r") as contents:

        #loops through lines
        for line in contents:
            #doesn't get the first line because it's irrelevant
            if first_line != 0:
                line = line.strip()
                content = line.split("\t")


                print(content)
                all_contents.append(content)
            first_line += 1


    print(all_contents)

def add():
    date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    print(f"That day is/was {date.strftime('%A')}")
    print(date.strftime("%d/%m/%Y"))
main()

