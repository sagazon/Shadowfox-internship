#!/bin/python3

# Avengers class
class Avenger:
    def __init__(self, name, age, gender, super_power, weapon, leader=False):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon
        self.leader = leader 

    # superhero information
    def get_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Super Power: {self.super_power}")
        print(f"Weapon: {self.weapon}")

    
    def is_leader(self):
        if self.leader:
            print(f"{self.name} is the leader of the Avengers!")
        else:
            print(f"{self.name} is not the leader.")

# Creating superheroes using the Avenger class
captain_america = Avenger("Captain America", 100, "Male", "Super Strength", "Shield", leader=True)
iron_man = Avenger("Iron Man", 45, "Male", "Technology", "Armor")
black_widow = Avenger("Black Widow", 35, "Female", "Superhuman", "Batons")
hulk = Avenger("Hulk", 40, "Male", "Unlimited Strength", "No Weapon")
thor = Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir")
hawkeye = Avenger("Hawkeye", 40, "Male", "Fighting Skills", "Bow and Arrows")

# Listing superheroes
super_heroes = [captain_america, iron_man, black_widow, hulk, thor, hawkeye]

# information about each superheros
for hero in super_heroes:
    hero.get_info()
    hero.is_leader()
    print("-" * 30)  

