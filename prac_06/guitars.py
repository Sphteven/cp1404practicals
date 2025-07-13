from prac_06.guitar import Guitar

guitars = []
guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
print("My guitars!")
# name = input("Name: ")
# while name != "":
#     year = input("Year: ")
#     cost = input("Cost: ")
#     new_guitar = Guitar(name, year, cost)
#     guitars.append(new_guitar)
#     print(f"{new_guitar} added.")
#     name = input("Name: ")
print(f"{guitars[0]} added.")
print(f"{guitars[1]} added.")
print(f"{guitars[2]} added.")
guitar_count = 1
max_name_length = max(len(guitar.name) for guitar in guitars)
max_cost_length = max(len(f"{guitar.cost:,.2f}") for guitar in guitars)
for guitar in guitars:
    if guitar.is_vintage():
        print(
            f"Guitar {guitar_count}: {guitar.name:>{max_name_length}}, worth $ {guitar.cost:>{max_cost_length},.2f} (vintage)")
    else:
        print(f"Guitar {guitar_count}: {guitar.name:>{max_name_length}}, worth $ {guitar.cost:>{max_cost_length},.2f}")
    guitar_count += 1
