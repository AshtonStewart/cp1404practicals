"""
CP1404 - Practical 4
Ashton Jack Stewart
total income report generator
"""
nests = []

FILENAME = "subject_data.txt"

def main():
    nest_info_to_print = load_data() #gets nested list
    # uses the information from the loaded data for the information_printer function
    information_printer(nest_info_to_print)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        #print(line)  # See what a line looks like
        #print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        #print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        #print(parts)  # See if that worked
        #print("----------")

        # adds all parts gathered from previous code and adds to the end of lists as a new chunk
        nests.append(parts)

    input_file.close() #closes the file
    return(nests) #returns information for the information_printer function to use

def information_printer(nested_information):
    for subject_information in nested_information: #loops through each group of data for the list
        #prints the first, second and third pieces of info available in the nest for each position along the list
        print(f"{subject_information[0]} is taught by {subject_information[1]} and has {subject_information[2]} students.")

main()