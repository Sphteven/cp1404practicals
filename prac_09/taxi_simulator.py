from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi


def main():
    MENU = "q)uit, c)hoose taxi, d)rive"
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    user_choice = input(MENU)
    while user_choice != "q":
        if user_choice == "c":
            list_taxis(taxis)

        elif user_choice == "d":
            return
        else:
            print("Invalid choice")
        user_choice = input(MENU)


def list_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
