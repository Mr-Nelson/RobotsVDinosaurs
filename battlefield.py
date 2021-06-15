import random

from herd import Herd
from fleet import Fleet

class Battlefield:
    def __init__(self):
        self.import_fleet = Fleet()
        self.import_fleet.robot_fleet()
        self.import_herd = Herd()
        self.import_herd.dino_herd()
        self.dead_robots = []
        self.dead_dinos = []
    def run_game(self):
        print("Welcome to the Thunder Dome!")
        self.battle()
        self.dino_turn()
        self.robot_turn()
        self.show_dino_opponent_options()
        self.show_robot_opponent_options()
        self.display_winners()

    def battle(self):
        self.fighting_robot = random.choices(self.import_fleet.robots)[0]
        self.fighting_dino = random.choices(self.import_herd.dinos)[0]

    def dino_turn(self):
        self.fighting_dino.dino_attack(self.fighting_robot)
        print(f"{self.fighting_dino.type} hits {self.fighting_robot.name} for {self.fighting_dino.attack_power} points.")
    def robot_turn(self):
        self.fighting_robot.robo_attack(self.fighting_dino)
        print(f"{self.fighting_robot.name} hits {self.fighting_dino.type} for {self.fighting_robot.weapon.attack_power} points.")
    def show_dino_opponent_options(self):
        if self.fighting_robot.health > 0 and self.fighting_dino.health > 0:
            self.dino_turn()
        if self.fighting_robot.health <= 0:
            self.import_fleet(self.fighting_robot)
            self.battle()
        if self.fighting_dino.health <= 0:
            self.import_herd.remove(self.fighting_dino)
            self.battle()

    def show_robot_opponent_options(self):
        if self.fighting_robot.health > 0 and self.fighting_dino.health > 0:
            self.robot_turn()
        if self.fighting_robot.health <= 0:
            self.import_fleet(self.fighting_robot)
            self.battle()
        if self.fighting_dino.health <= 0:
            self.import_herd.remove(self.fighting_dino)
            self.battle()

    def display_winners(self):
        if self.import_fleet == 0:
            print("The dinosaurs defeated your robots!")
        if self.import_herd == 0:
            print("Your fleet of robots won!")