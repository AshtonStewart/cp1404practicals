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
            page_details = wikipedia.page(search_prompt)
            print(f"Webpage title:\n{page_details.title}\n\nUrl:\n{page_details.url}\n\nSummary:\n{page_details.summary}")
        except wikipedia.exceptions.DisambiguationError as e:
            print("Disambiguation Error")
        except wikipedia.exceptions.PageError:
            print("Page ID doesn't exist")
        search_prompt = input("Wikipedia content you'd like to search for: ")
    print("Thank you.")


main()
