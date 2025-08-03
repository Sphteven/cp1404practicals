from silver_service_taxi import SilverServiceTaxi

my_taxi = SilverServiceTaxi("Hummer", 200, 4)
print(my_taxi)

other_taxi = SilverServiceTaxi("Premium", 200, 2)
print(other_taxi)
other_taxi.drive(18)
print(f"The total cost for the distance is ${other_taxi.get_fare()}")
