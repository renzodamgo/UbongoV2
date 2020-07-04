import Algoritmo as al
import random

class Player:
    def __init__(self):
        self.gemas = []
        self.posY = 0

        self.fichas = []

    def mover(self,dir):
        if dir == "abajo":
            self.posY += 1
        if dir == "arriba":
            self.posY -= 1

    def recolectarGemas(self, gemas):
        self.gemas.append(gemas)

    def resolverPuzzle(self, piezas, plantilla):
        pass


class Human(Player):

    def resolverPuzzle(self, piezas, plantilla):
        pass


class Computer(Player):
    def __init__(self):

        super().__init__()
        self.posY = random.randrange(0,6)

    def resolverPuzzle(self, piezas, plantilla):
        return al.resolverPuzzle(piezas, plantilla)


