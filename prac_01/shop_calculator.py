
total_cost = 0
num_of_items = int(input("Number of items: "))
while num_of_items <= 0:
    print("Invalid input")
    num_of_items = int(input("Number of items: "))
for i in range(0, num_of_items, 1):
    item_cost = float(input("Price of item: "))
    while item_cost < 0:
        print("Invalid cost")
        item_cost = float(input("Price of item"))
    total_cost += item_cost
print(f"Total price for {num_of_items} items ${total_cost:.2f}")
