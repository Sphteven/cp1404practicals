from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi


def main():
    MENU = "q)uit, c)hoose taxi, d)rive \n"
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    total_bill = 0
    print("Let's drive!")
    user_choice = input(MENU).upper()
    while user_choice != "Q":
        if user_choice == "C":
            print("Taxis available: ")
            list_taxis(taxis)
            chosen_taxi = input("Choose taxi: ")
            try:
                current_taxi = taxis[int(chosen_taxi)]
            except IndexError and ValueError:
                print("Invalid taxi choice")

        elif user_choice == "D":
            if current_taxi is not None:
                try:
                    drive_taxi(current_taxi)
                    total_bill = get_total_bill(taxis)
                except ValueError:
                    print("Invalid distance")
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid choice")

        print(f"Bill to date: ${total_bill:.2f}")
        user_choice = input(MENU).upper()
    print(f"Total trips cost: ${total_bill:.2f}")
    print("Taxis are now:")
    list_taxis(taxis)


def drive_taxi(current_taxi):
    distance_driven = int(input("Drive how far? "))
    current_taxi.drive(distance_driven)
    print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}")


def list_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def get_total_bill(taxis):
    total_bill = 0
    for taxi in taxis:
        if taxi.current_fare_distance != 0:
            total_bill += taxi.get_fare()
    return total_bill


main()
