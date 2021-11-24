#!python3

"""
Create a class that will store a database for a veterinarian.
Your class will need the following properties:

animal (dog, cat, fish, bird, turtle, etc)
breed
name (the pet's name)
owner (the owner's name)
birthdate (of the pet, expressed as yyyy-mm-dd)

The constructor will need to ask for each of those values
for the database when the pet is instantiated

Methods:
display() - should show the name of the pet and type followed by their breed and owner


Main block should have a menu that has the following options:
1. Enter a new pet
2. Retrieve a pet
3. Exit

If they choose to retrieve a pet,
display the following:
Enter pet's name:
and then go through the list, looking for the name of the pet.
If the pet is found, it should call the display() method from the object

Example output:
1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Benjamin
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? dog
Breed? Shih-tzu
Name? Buster
Owner? Christy
Birthdate? 2008-10-16

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Casey
Owner? Chris
Birthdate? 2015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
2

Which Pet? Buster

Buster dog
Shih-tzu is owned by Christy
(10 points) 
"""
def menu():
    print("1. Enter a new pet")
    print("2. Retrieve a pet")
    print("3. Exit")


class Pets:

    animal = ""
    breed = ""
    name = ""
    owner = ""
    bday = ""

    def __init__(self):
        self.animal = input("Type of animal?")
        self.breed = input("Breed?")
        self.name = input("Name?")
        self.owner = input("Owner?")
        self.bday = input("Birthdate?")

plist = []

while True:
    menu()
    choice = input("")
    if choice == "1":
        plist.append(Pets())
    
    if choice == "2":
        find = input("Which pet?")
        for i in plist:
            if find == plist[i].name:
                print(plist[i].name + " " + plist[i].animal)
                print(plist[i].breed + " is owned by " + plist[i].owner)

    if choice == "3":
        break
        



    