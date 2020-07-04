import Algoritmo as al


class Player:
    def __init__(self):
        self.gemas = []
        self.posX = 0
        self.posY = 0

        self.fichas = []

    def mover(self, cant):
        self.posY = self.posY + cant

    def recolectarGemas(self):
        pass

    def resolverPuzzle(self, piezas, plantilla):
        print("a")


class Human(Player):
    def hello(self):
        print("hello")

    def resolverPuzzle(self, piezas, plantilla):
        pass


class Computer(Player):

    def resolverPuzzle(self, piezas, plantilla):
        return al.resolverPuzzle(piezas, plantilla)


if __name__ == "__main__":
    a = Human()
    b = Computer()
    b.resolverPuzzle()
    a.hello()
    print(a.pos)
