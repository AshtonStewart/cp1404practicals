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

        print(f"\n {menu}")
        chosen_action = input(">> ").upper()

        if chosen_action == "L":
            all_projects = info_get()

        elif chosen_action == "S":
            save(all_projects)

        elif chosen_action == "D":
            display(all_projects)

        elif chosen_action == "F":
            filter_display(all_projects)

        elif chosen_action == "A":
            all_projects = add(all_projects)

        elif chosen_action == "U":
            print("Update")
            all_projects = update(all_projects)

        elif chosen_action != "Q":
            print("Invalid menu choice")
    print("Process concluded")

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

                new_content = Project(name=content[0], S_D_P=content[1], priority=float(content[2]), C_E=float(content[3]), C_P=float(content[4])
                )
                all_contents.append(new_content)
            first_line += 1

    return all_contents

def save(all_projects):
    print("save")
    with open(file_name, "w") as out_file:

        for new_line in all_projects:
            out_file.write(new_line.to_line() + '\n')



def display(info_to_display):

    incomplete_projects = [item for item in info_to_display if not item.is_completed()]
    complete_projects = [item for item in info_to_display if item.is_completed()]


    print("\n\nIncomplete projects: ")

    for each_project in incomplete_projects:
        print(each_project)

    print("\n\nComplete projects: ")
    for each_project in complete_projects:
        print(each_project)


def filter_display(all_contents):

    date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()

def add(current_contents):
    new_project_info = []
    date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    #print(f"That day is/was {date.strftime('%A')}")
    #print(date.strftime("%d/%m/%Y"))

    new_project_info.append(input("New project name: "))
    new_project_info.append(date)
    new_project_info.append(float(input("What number priority is it: ")))
    new_project_info.append(float(input("What is the expected cost: ")))
    new_project_info.append(float(input("What is the percentage completion (do not type '%'): ")))

    current_contents.append(Project(new_project_info[0], new_project_info[1], new_project_info[2], new_project_info[3], new_project_info[4]))

    return current_contents


def update(current_contents):

    matches_name = False


    while matches_name == False:
        project_to_update = input("Please type the name of the project you'd like to update: ")
        #print(current_contents)
        for project in current_contents:
            if project.name == project_to_update:
                matches_name = True

    new_C_P = float(input(f"What is the new completion % of {project_to_update} (do not add '%'): "))

    for project in current_contents:
        if project.name == project_to_update:
            project.C_P = new_C_P

    return current_contents






main()