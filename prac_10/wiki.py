"""
CP1404 - Practical 10
Ashton Jack Stewart
Wikipedia improrting API test
"""

import wikipedia


def main():
    """Search wikipedia for content relevant to user input"""
    search_prompt = input("Wikipedia content you'd like to search for: ")
    while search_prompt.strip(" ") != "":

        try:
            print(wikipedia.summary(search_prompt))
        except wikipedia.exceptions.DisambiguationError as e:
            print("error")
        search_prompt = input("Wikipedia content you'd like to search for: ")


main()
