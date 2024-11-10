"""
Ashton Jack Stewart
Project data saving and modification
"""
import datetime
from project import Project

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
    #Displays a menu / list of options for the user to choose from
    all_projects = []
    chosen_action = "Not nothing"
    while chosen_action != "Q":
        print(menu)
        chosen_action = input(">> ").upper()

        if chosen_action == "L":
            all_projects = info_get()

        elif chosen_action == "S":
            print("save")

        elif chosen_action == "D":
            print("Display")
            display(all_projects)

        elif chosen_action == "F":
            print("Filter by date")

        elif chosen_action == "A":
            print("Add new project")
            all_projects = add(all_projects)

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

                #print(content)
                all_contents.append(content)
            first_line += 1

    return all_contents

def save():
    print("save")

def display(info_to_display):

    for line in info_to_display:
        #def __init__(self, name, S_D_P, C_E, priority, C_P):
        print(line[0])

        #print(Project(line[0].name, info_to_display[1].S_D_P, info_to_display[2].C_E, info_to_display[3].priority, info_to_display[4].C_P))
        #print(line)

def add(current_contents):
    new_project_info = []
    date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    #print(f"That day is/was {date.strftime('%A')}")
    #print(date.strftime("%d/%m/%Y"))

    #new_project_info.append((
    new_project_info.append(input("New project name: "))
    new_project_info.append(date_string)
    new_project_info.append(float(input("What number priority is it: ")))
    new_project_info.append(float(input("What is the expected cost: ")))
    new_project_info.append(float(input("What is the percentage completion (do not type '%'): ")))

    current_contents.append(Project(new_project_info))

    print(current_contents)
    return current_contents

main()


#  print(info_to_display)
#     for line in info_to_display:
#         print(line.name)
#
# def add(current_contents):
#     new_project_info = []
#     date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
#     date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
#     #print(f"That day is/was {date.strftime('%A')}")
#     #print(date.strftime("%d/%m/%Y"))
#     S_D_P = date
#     #new_project_info.append((
#     name = input("New project name: ")
#
#     #new_project_info.append(date_string)
#
#     C_E = float(input("What is the expected cost: "))
#     priority = float(input("What number priority is it: "))
#     C_P = float(input("What is the percentage completion (do not type '%'): "))
#
#     current_contents.append(Project(name, S_D_P, C_E, priority, C_P))
#
#     print(current_contents)
#     return current_contents
#
# main()
# #print(Project(name, S_D_P, C_E, priority, C_P))