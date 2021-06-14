from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []

    def robot_fleet(self):
        robot_one = Robot("IronGiant")
        robot_one.weapon_choice("punch", 30)
        robot_two = Robot("Mechazilla")
        robot_two.weapon_choice("nuclear breath", 40)
        robot_three = Robot("Wall-e")
        robot_three.weapon_choice("curiousity", 0.5)
        self.robots.append(robot_one)
        self.robots.append(robot_two)
        self.robots.append(robot_three)