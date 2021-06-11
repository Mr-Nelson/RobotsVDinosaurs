from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.power_level = 100
        self.weapon = []

    def robot_name(self):
        self.name = input("Enter your robot's name:")
        print (f"Your robot's name is {self.name}!")

    """def robot_power_up(self):
        self.power_level and self.health = input("Are you ready to power up your robot?")
        if input == "yes":
            self.power_level and self.health == 100
            print(f"{self.name} is full on health and power!")
        else:
            print(f"{self.name}) has no health or power!")"""
    def weapon_choice(self):
        weapon_one = Weapon()
        weapon_one.rando_weapons()
        weapon_one.attack_power()

    def robo_attack(self):
#         robot attacks dino
pass
