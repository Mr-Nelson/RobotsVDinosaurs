from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []

    def robot_fleet(self):
        robot_one = Robot()
        robot_one.robot_name()
        robot_one.weapon_choice()
        robot_two = Robot()
        robot_two.robot_name()
        robot_two.weapon_choice()
        robot_three = Robot()
        robot_three.robot_name()
        robot_three.weapon_choice()
