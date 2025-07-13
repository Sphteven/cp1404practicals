from prac_06.car import Car

MENU = ("Menu: \n"
        "d) drive \n"
        "r) refuel \n"
        "q) quit \n"
        "Enter your choice: ")

my_car = Car(100, "Mazda")
print(my_car)

choice = input(MENU).lower()
while choice != "q":
    if choice == "d":
        distance = int(input("How many km do you wish to drive? "))
        while distance <= 0:
            print("Distance must be > 0")
            distance = int(input("How many km do you wish to drive? "))
        distance_drove = distance
        if distance_drove > my_car.fuel:
            distance_drove = distance_drove - (distance_drove - my_car.fuel)
        my_car.drive(distance)
        if my_car.fuel == 0:
            print(f"The car drove {distance_drove}km and ran out of fuel \n")
        else:
            print(f"The car drive {distance_drove}km \n")
    elif choice == "r":
        fuel = int(input("How many units of fuel do you want to add to your car? "))
        while fuel < 0:
            print("Fuel must be >= 0")
            fuel = int(input("How many units of fuel do you want to add to your car? "))
        my_car.add_fuel(fuel)
        print(f"Added {fuel} units of fuel \n")
    else:
        print("Invalid choice")
    print(my_car)
    choice = input(MENU).lower()
print(f"Good bye {my_car.name} driver.")
