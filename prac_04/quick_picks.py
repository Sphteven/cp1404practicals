import random
OUTPUT = []
total_quick_picks = int(input('How many quick picks? '))

for i in range(total_quick_picks):
    numbers = []
    for num in range(total_quick_picks):
        rand_number = random.randint(1, 45)
        while rand_number in numbers:
            rand_number = random.randint(1, 45)
        numbers.append(rand_number)
    numbers.sort()
    OUTPUT.append(numbers)
    for number in numbers:
        print(f"{number:>2}", end=" ")

    print("")

print(OUTPUT)
