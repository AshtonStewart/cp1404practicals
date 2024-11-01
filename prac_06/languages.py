"""
Ashton Jack Stewart
Practical 06 - languages
started: 2:46pm
Finished: 11:28am
"""

from programming_language import Programminglanguage
def print_info():
    #gives variables and their values
    python = Programminglanguage("Python", "Dynamic", True, 1991)
    ruby = Programminglanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = Programminglanguage("Visual Basic", "Static", False, 1991)

    #list of names
    languages = [python, ruby, visual_basic]

    print("The Dynamic languages are:")
    #makes a list of variable names that are Dynamic"
    to_be_printed = [language.name for language in languages if language.is_dynamic()]
    #prints that list
    print(to_be_printed)
    #print(python)

print_info()
