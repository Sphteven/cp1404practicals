"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
It will occur whenever the expected input type does not match which what the program expects.
2. When will a ZeroDivisionError occur?
Will only occur when the program attempts to divide by zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, by utilising a while loop to determine that the input is in fact not 0.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")