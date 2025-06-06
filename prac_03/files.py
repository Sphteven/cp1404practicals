FILENAME = "name.txt"

name = input("Enter your name: ")
file = open(FILENAME, "w")
file.write(name)
file.close()

file = open(FILENAME, "r")
line = file.read()
print(f"Hi {line}!")
file.close()

with open("numbers.txt", "r") as f:
    first_num = int(f.readline())
    second_num = int(f.readline())
    result = first_num + second_num
    print(f"The result is {result}")
