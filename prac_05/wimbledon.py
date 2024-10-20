"""
cp1404 - Ashton Jack Stewart
Processing csv files using nests and dictionaries
"""



import csv


def main():
    champions_and_wins_total, winning_countries = get_data()
    champion_data_printer(champions_and_wins_total)
    country_data_printer(winning_countries)

def get_data():
    #creates empty dictionary
    champions_and_wins_total = {}
    #creates empty list
    winning_countries = []
    #opens and reads the csv file
    with open('wimbledon.csv', "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        #loops through each line and gets relevant information and stores in a list
        for each_line in reader:
            country = each_line[1]
            champion_name = each_line[2]
            #adds countries if not in the list
            if country not in winning_countries:
                winning_countries.append(country)
            if champion_name in list(champions_and_wins_total.keys()):
                champions_and_wins_total[champion_name] += 1
            else:
                champions_and_wins_total[champion_name] = 1
    #returns stuff for the main function to use in other functions
    return champions_and_wins_total, winning_countries


def country_data_printer(country_data):
    print("The 12 winning countries are:")
    #sorts data alphabetically:
    country_data.sort()
    #prints all contents in a row at once:
    print(*country_data)

def champion_data_printer(win_data):
    print("Champions:")
    #prints every champion name (key) and their wins(value) from the dictionary
    for champion_name, wins in win_data.items():
        print(f"{champion_name} won {wins} times!")

main()