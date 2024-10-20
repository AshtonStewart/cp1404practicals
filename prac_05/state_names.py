"""
CP1404 - Ashton Stewart
State names in a dictionary
reformatted files
"""

code_to_name = {"QLD": "Queensland",
                "NSW": "New South Wales",
                "NT": "Northern Territory",
                "WA": "Western Australia",
                "ACT": "Australian Capital Territory",
                "VIC": "Victoria",
                "TAS": "Tasmania", "SA": "South Australia"}
#print(code_to_name) #commented out as it now seemed unnecessary

for code, state_name in code_to_name.items():
    print(f" {code:3} is {state_name}")

state_code = input("Enter short state: ").upper() #added .upper() to always change input to capitals

while state_code != "":
    if state_code in code_to_name:
        print(state_code, "is", code_to_name[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper() #added .upper() to always change input to capitals

