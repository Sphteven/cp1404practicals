for i in range(1, 21, 2):
    print(i, end=' ')
print()

print("Count in 10s to 100")

for i in range(0, 110, 10):
    print(i, end=' ')
print()

print("Count down from 20 to 1")
for i in range(20, 0, -1):
    print(i, end=' ')
print()

num = int(input("How many stars would you like? "))
for i in range(0, num, 1):
    print("*", end=' ')
print()
for i in range(0, num+1, 1):
    for n in range(0, i, 1):
        print("*", end='')
    print()
print()
