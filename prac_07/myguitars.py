from guitar import Guitar


def main():
    FILENAME = "guitars.csv"
    guitars = []
    in_file = open(FILENAME, "r")
    for line in in_file:
        parts = line.strip().split(",")
        year = int(parts[1])
        cost = float(parts[2])
        guitar = Guitar(parts[0], year, cost)
        guitars.append(guitar)
    in_file.close()
    guitars.sort()
    for guitar in guitars:
        print(guitar)


main()
