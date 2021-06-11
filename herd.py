from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinos = []

    def dino_herd(self):
        dino_one = Dinosaur()
        dino_one.dino_type()
        dino_one.dino_attack()
        dino_two = Dinosaur()
        dino_two.dino_type()
        dino_two.dino_attack()
        dino_three = Dinosaur()
        dino_three.dino_type()
        dino_three.dino_attack()
