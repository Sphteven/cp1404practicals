from prac_06.person import Person

people = []
people.append(Person("Jerry", "Fair", 25))
people.append(Person("John", "Smith", 45))
people.append(Person("Steve", "Harry", 28))
people.append(Person("Rick", "Jones", 12))
people.append(Person("Spongebob", "Squarepants", 16))

# first_name = input("First Name: ")
# while first_name != "":
#     last_name = input("Second Name: ")
#     age = int(input("Age: "))
#     people.append(Person(first_name, last_name, age))
#     print(f"{first_name} {last_name} has been added to the list of people")
#     first_name = input("First Name: ")

people.sort(key=lambda person: person.age)
print("Here is a list of all the people from youngest to oldest: ")
max_first_name_length = max(len(person.first_name) for person in people)
max_last_name_length = max(len(person.last_name) for person in people)
for i, person in enumerate(people, 1):
    print(f"{i}. {person.first_name:<{max_first_name_length}} {person.last_name:<{max_last_name_length}} is {person.age} years old.")

