from guitar import Guitar


def main():
    FILENAME = "guitars.csv"
    guitars = load_from_file(FILENAME)
    guitars.sort()

    print("")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")
        name = input("Name: ")

    output_to_file(FILENAME, guitars)
    print("These files have been added: ")
    list_guitars(guitars)


def output_to_file(FILENAME, guitars):
    with open(FILENAME, "w") as guitars_file:
        for guitar in guitars:
            guitars_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


def list_guitars(guitars):
    for guitar in guitars:
        print(guitar)


def load_from_file(FILENAME):
    guitars = []
    in_file = open(FILENAME, "r")
    for line in in_file:
        parts = line.strip().split(",")
        year = int(parts[1])
        cost = float(parts[2])
        guitar = Guitar(parts[0], year, cost)
        guitars.append(guitar)
    in_file.close()
    return guitars


main()
