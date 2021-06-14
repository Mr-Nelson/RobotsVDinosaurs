import battlefield
from battlefield import Battlefield

class Dinosaur:
    def __init__(self, type, attack_power):
        self.type = type
        self.health = 100
        self.energy = 100
        self.attack_power = attack_power
"""
    def dino_type(self):
        self.type = input("Enter your dino competitor here.")
        print (f"You chose the {self.type}!")

    def attack_power(self):
        self.attack_power = input("Choose a number between 1 and 100.")
        number = int(input)
        print(f"Your {self.type} has {number} attack power!")
"""

    def dino_attack(self):
        battlefield.Battlefield.dino_turn(self.fighting_robot).health -= battlefield.Battlefield.dino_turn(self.fighting_dino).attack_power
        pass