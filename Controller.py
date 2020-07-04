import random as rand


class Controller:
    def __init__(self):
        self.gemas = []
        self.n_ronda = 0
        self.jugar = True
        self.temporizador = 30

    def roll_dice(self):
        return rand.randrange(0, 5)

    def asignar_objetos(self, r_dado, valplantilla):
        pass
