from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinos = []

    def dino_herd(self):
        dino_one = Dinosaur("T-rex", 40)
        dino_two = Dinosaur("Brontosaurus", 30)
        dino_three = Dinosaur("Raptor", 25)
        self.dinos.append(dino_one)
        self.dinos.append(dino_two)
        self.dinos.append(dino_three)