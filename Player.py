import Algoritmo as al


class Player:
    def __init__(self):
        self.gemas = []
        self.posY = 0

        self.fichas = []

    def mover(self, cant):
        self.posY = self.posY + cant

    def recolectarGemas(self, gemas):
        self.gemas.append(gemas)

    def resolverPuzzle(self, piezas, plantilla):
        pass


class Human(Player):

    def resolverPuzzle(self, piezas, plantilla):
        pass


class Computer(Player):

    def resolverPuzzle(self, piezas, plantilla):
        return al.resolverPuzzle(piezas, plantilla)


