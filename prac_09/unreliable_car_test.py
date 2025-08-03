from prac_09.unreliable_car import UnreliableCar

my_car = UnreliableCar("Ford Falcon", 100, 30)
print(my_car)
car_driven = 0
for i in range(100):
    try:
        if my_car.drive(1) == 1:
            car_driven += 1
    except TypeError:
        print("fail")

print(f"Car drove a total of {car_driven} times")