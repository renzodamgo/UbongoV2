class Player:
    def __init__(self):
        self.gemas = []
        self.pos = 0
        self.fichas = []

    def mover(self):
        pass

    def recolectarGemas(self):
        pass

    def resolverPuzzle(self):
        print("a")


class Human(Player):
    def hello(self):
        print("hello")

    def resolverPuzzle(self):
        pass


class Computer(Player):
    def resolverPuzzle(self):
        print("resolver Computer")


if __name__ == "__main__":
    a = Human()
    b = Computer()
    b.resolverPuzzle()
    a.hello()
    print(a.pos)
