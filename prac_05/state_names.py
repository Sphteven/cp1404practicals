"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}

for i in CODE_TO_NAME:
    print(f"{i:<3} is {CODE_TO_NAME[i]}")

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        state = CODE_TO_NAME[state_code]
        print(state_code, "is", state)
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
