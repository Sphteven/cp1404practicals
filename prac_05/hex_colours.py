"""
CP1404/CP5632 Practical
Hex codes in dictionary
"""


HEX_NAME_TO_CODE = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "aliceblue": "#f0f8ff",
                    "amber": "#9966cc", "amethyst": "#9966cc", "aqua": "#00ffff",
                    "azure1": "#f0ffff", "baby blue": "#89cff0", "baby pink": "#f4c2c2",
                    "banana yellow": "#ffe135"}
print(HEX_NAME_TO_CODE)

for key in HEX_NAME_TO_CODE:
    print(f"{key:<13} is {HEX_NAME_TO_CODE[key]}")

hex_name = input("Enter hex name: ").lower()
while hex_name != "":
    try:
        hex_code = HEX_NAME_TO_CODE[hex_name].lower()
        print(hex_name, " hex code is", hex_code)
    except KeyError:
        print("Invalid hex name")
    hex_name = input("Enter hex name: ").lower()

