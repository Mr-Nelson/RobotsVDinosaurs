import random
from herd import Herd
from fleet import Fleet

class Battlefield:
    def __init__(self):
        self.import_fleet = Fleet()
        self.import_fleet.robot_fleet()
        self.import_herd = Herd()
        self.import_herd.dino_herd()

    def run_game(self):
            print ("Welcome to the Thunder Dome!")

    def battle(self):
        self.fighting_robot = random.randrange(self.import_fleet)
        self.fighting_dino = random.randrange(self.import_herd)

    def dino_turn(self):
        self.fighting_dino.dino_attack
        print(f"{self.fighting_dino.type} hits {self.fighting_robot.name} for {self.fighting_dino.attaack_power} points.")
    def robot_turn(self):
        self.fighting_robot.robo_attack
        print(f"{self.fighting_robot.name} hits {self.fighting_dino.type} for {self.fighting_robot.attaack_power} points.")
    def show_dino_opponent_options(self):
        pass
    def show_robot_opponent_options(self):
        pass
    def display_winners(self):
        pass