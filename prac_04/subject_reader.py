"""
CP1404 - Practical 4
Ashton Jack Stewart
subject reader"""
nests = []

FILENAME = "subject_data.txt"

def main():
    information_nests = load_data()
    information_printer(information_nests)

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

    input_file.close()
    return(nests)

def information_printer(information_nests):
    for i in information_nests:
        #print("current list")
        #print(i)
        #print(i[0])
        #print(i[1])
        #print(i[2])
        print(f"{i[0]} is taught by {i[1]} and has {i[2]} students.")

main()