import random

import battlefield
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
        battlefield.Battlefield.battle(self)
        battlefield.Battlefield.dino_turn(self)
        battlefield.Battlefield.robot_turn(self)
        battlefield.Battlefield.show_dino_opponent_options(self)
        battlefield.Battlefield.show_robo_opponent_options(self)
    def battle(self):
        self.fighting_robot = random.randrange(self.import_fleet[])
        self.fighting_dino = random.randrange(self.import_herd[])

    def dino_turn(self):
        dino = self.fighting_dino
        robot = self.fighting_robot
        self.fighting_dino.dino_attack
        print(f"{self.fighting_dino.type} hits {self.fighting_robot.name} for {self.fighting_dino.attaack_power} points.")
    def robot_turn(self):
        dino = self.fighting_dino
        robot = self.fighting_robot
        print(f"{self.fighting_robot.name} hits {self.fighting_dino.type} for {self.fighting_robot.attaack_power} points.")
    def show_dino_opponent_options(self):
        if self.fighting_robot.health > 0 and self.fighting_dino.health > 0:
            battlefield.Battlefield.dino_turn()
        if self.fighting_robot.health == 0 or self.fighting_dino.health == 0:
            battlefield.Battlefield.battle()

    def show_robot_opponent_options(self):
        if self.fighting_robot.health > 0 and self.fighting_dino.health > 0:
           battlefield.Battlefield.robot_turn()
        if self.fighting_robot.health == 0 or self.fighting_dino.health == 0:
          battlefield.Battlefield.battle()

    def display_winners(self):
        if Fleet.robot_one.health == 0 and Fleet.robot_two.health == 0 and Fleet.robot_three.health == 0:
            print ("The dinosaurs defeated your robots!")
        if Herd.dino_one.health == 0 and Herd.dino_two.health == 0 and Herd.dino_three.health == 0:
            print ("Your fleet of robots won!")