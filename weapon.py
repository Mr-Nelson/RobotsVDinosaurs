class Weapon:
    def __init__(self, type, attack_power):
        self.weapon_type = type
        self.attack_power = attack_power

    def rando_weapons(self):
        self.weapon_type = input ("Choose your weapon.")
        print(f"Your robot has the {self.weapon_type}!")

    def attack_power(self):
        self.attack_power = input ("Choose a number between 1 and 100.")
        number = int(input)
        print (f"Your robot has {number} attack power!")
