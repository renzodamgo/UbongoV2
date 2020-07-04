import random as rand
import numpy as np
import Player
import random


class Controller:
    def __init__(self):
        self.gemas = []
        self.n_ronda = 0
        self.jugar = True
        self.temporizador = 30
        self.Jugadores = [Player.Human(), Player.Computer()]
        self.posC = 0
        self.posJ = 0
        self.posC = random.randrange(0, 6)

    def mover(self, dir):
        self.Jugadores[0].mover(dir)

    def play(self):
        pass

    def elegir_pos(self, pos):
        return self.posC

    def roll_dice(self):
        return rand.randrange(0, 5)

    def asignar_objetos(self, rd, rp):
        if rp == 0:
            if rd == 0:  # dado 1
                piezaa = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 0]])
                piezab = np.array([[1, 1, 0], [1, 1, 1]])
                piezac = np.array([[1, 1, 1]])
            if rd == 1:  # dado 2
                piezaa = np.array([[0, 1], [1, 1], [1, 0]])
                piezab = np.array([[0, 1], [1, 1], [1, 0]])
                piezac = np.array([[1, 0], [1, 0], [1, 1]])
            if rd == 2:  # dado 3
                piezaa = np.array([[1, 1, 0], [1, 1, 1]])
                piezab = np.array([[0, 0, 0, 1], [1, 1, 1, 1]])
                piezac = np.array([[1, 0], [1, 1], [1, 0]])
            if rd == 3:  # dado 4
                piezaa = np.array([[0, 1], [1, 1]])
                piezab = np.array([[1, 1, 1, 1], [0, 0, 1, 0]])
                piezac = np.array([[1, 1, 0], [1, 1, 1]])
            if rd == 4:  # dado 5
                piezaa = np.array([[1, 1, 1, 1]])
                piezab = np.array([[0, 1], [1, 1], [1, 0]])
                piezac = np.array([[1, 1, 0], [1, 1, 1]])
            if rd == 5:  # dado 6
                piezaa = np.array([[0, 1], [1, 1], [1, 0]])
                piezab = np.array([[1, 1], [1, 1]])
                piezac = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 0]])

        if rp == 1:
            if rd == 0:  # dado 1
                piezaa = np.array([[1, 1, 1, 1]])
                piezab = np.array([[1, 1, 0], [1, 1, 1]])
                piezac = np.array([[1, 0], [1, 1], [1, 0]])
            if rd == 1:  # dado 2
                piezaa = np.array([[1, 0], [1, 0], [1, 1]])
                piezab = np.array([[1, 0], [1, 1], [1, 0]])
                piezac = np.array([[1, 1, 0], [1, 1, 1]])
            if rd == 2:  # dado 3
                piezaa = np.array([[1, 1, 1, 1], [0, 0, 1, 0]])
                piezab = np.array([[0, 1], [1, 1], [1, 0]])
                piezac = np.array([[1, 1, 1, 1]])
            if rd == 3:  # dado 4
                piezaa = np.array([[1, 1, 1]])
                piezab = np.array([[1, 1, 0], [1, 1, 1]])
                piezac = np.array([[1, 1, 1, 1], [0, 0, 1, 0]])
            if rd == 4:  # dado 5
                piezaa = np.array([[1, 0], [1, 0], [1, 1]])
                piezab = np.array([[1, 1, 1, 1]])
                piezac = np.array([[1, 1, 0], [1, 1, 1]])
            if rd == 5:  # dado 6
                piezaa = np.array([[0, 1], [1, 1], [1, 0]])
                piezab = np.array([[1, 0], [1, 0], [1, 1]])
                piezac = np.array([[1, 1, 0], [1, 1, 1]])

        if rp == 2:
            if rd == 0:  # dado 1
                piezaa = np.array([[1, 0], [1, 0], [1, 1]])
                piezab = np.array([[1, 1, 0], [1, 1, 1]])
                piezac = np.array([[1, 0], [1, 1], [1, 0]])
            if rd == 1:  # dado 2
                piezaa = np.array([[0, 1], [1, 1], [1, 0]])
                piezab = np.array([[1, 0], [1, 1], [1, 0]])
                piezac = np.array([[1, 1, 0], [1, 1, 1]])
            if rd == 2:  # dado 3
                piezaa = np.array([[1, 0], [1, 1], [1, 0]])
                piezab = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 0]])
                piezac = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 0]])
            if rd == 3:  # dado 4
                piezaa = np.array([[1, 0], [1, 0], [1, 1]])
                piezab = np.array([[0, 0, 0, 1], [1, 1, 1, 1]])
                piezac = np.array([[1, 1, 1, 1]])
            if rd == 4:  # dado 5
                piezaa = np.array([[0, 1], [1, 1]])
                piezab = np.array([[1, 1, 1, 1], [0, 0, 1, 0]])
                piezac = np.array([[0, 0, 0, 1], [1, 1, 1, 1]])
            if rd == 5:  # dado 6
                piezaa = np.array([[0, 0, 0, 1], [1, 1, 1, 1]])
                piezab = np.array([[1, 1], [1, 1]])
                piezac = np.array([[1, 0], [1, 0], [1, 1]])

        if rp == 3:
            if rd == 0:  # dado 1
                piezaa = np.array([[1, 0], [1, 1], [1, 0]])
                piezab = np.array([[0, 1], [1, 1], [1, 0]])
                piezac = np.array([[1, 1], [1, 1]])
                piezad = np.array([[0, 0, 0, 1], [1, 1, 1, 1]])
            if rd == 1:  # dado 2
                piezaa = np.array([[1, 1, 1]])
                piezab = np.array([[1, 1, 1, 1], [0, 0, 1, 0]])
                piezac = np.array([[1, 1, 0], [1, 1, 1]])
                piezad = np.array([[1, 0], [1, 1], [1, 0]])
            if rd == 2:  # dado 3
                piezaa = np.array([[1, 0], [1, 1], [1, 0]])
                piezab = np.array([[1, 1, 0], [1, 1, 1]])
                piezac = np.array([[0, 1], [1, 1]])
                piezad = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 0]])
            if rd == 3:  # dado 4
                piezaa = np.array([[0, 1], [1, 1], [1, 0]])
                piezab = np.array([[1, 1, 1, 1], [0, 0, 1, 0]])
                piezac = np.array([[1, 1, 1]])
                piezad = np.array([[0, 0, 0, 1], [1, 1, 1, 1]])
            if rd == 4:  # dado 5
                piezaa = np.array([[1, 0], [1, 0], [1, 1]])
                piezab = np.array([[1, 1, 0], [1, 1, 1]])
                piezac = np.array([[1, 1, 1, 1], [0, 0, 1, 0]])
                piezad = np.array([[0, 1], [1, 1]])
            if rd == 5:  # dado 6
                piezaa = np.array([[0, 1], [1, 1], [1, 0]])
                piezab = np.array([[1, 0], [1, 0], [1, 1]])
                piezac = np.array([[1, 1, 0], [1, 1, 1]])
                piezad = np.array([[1, 1], [1, 1]])

        if rp == 4:
            if rd == 0:  # dado 1
                piezaa = np.array([[0, 0, 0, 1], [1, 1, 1, 1]])
                piezab = np.array([[1, 0], [1, 1], [1, 0]])
                piezac = np.array([[1, 1, 1]])
                piezad = np.array([[1, 1, 0], [1, 1, 1]])
            if rd == 1:  # dado 2
                piezaa = np.array([[1, 1, 1]])
                piezab = np.array([[1, 1, 1, 1], [0, 0, 1, 0]])
                piezac = np.array([[1, 1, 0], [1, 1, 1]])
                piezad = np.array([[1, 0], [1, 1], [1, 0]])
            if rd == 2:  # dado 3
                piezaa = np.array([[1, 1, 1, 1], [0, 0, 1, 0]])
                piezab = np.array([[1], [1]])
                piezac = np.array([[1, 1, 0], [1, 1, 1]])
                piezad = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 0]])
            if rd == 3:  # dado 4
                piezaa = np.array([[1, 0], [1, 1], [1, 0]])
                piezab = np.array([[1, 1, 1, 1]])
                piezac = np.array([[0, 1], [1, 1], [1, 0]])
                piezad = np.array([[1, 1], [1, 1]])
            if rd == 4:  # dado 5
                piezaa = np.array([[0, 1], [1, 1]])
                piezab = np.array([[1, 1, 1, 1], [0, 0, 1, 0]])
                piezac = np.array([[1, 1], [1, 1]])
                piezad = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 0]])
            if rd == 5:  # dado 6
                piezaa = np.array([[0, 1], [1, 1], [1, 0]])
                piezab = np.array([[1, 1, 0], [1, 1, 1]])
                piezac = np.array([[1, 1], [1, 1]])
                piezad = np.array([[1, 0], [1, 0], [1, 1]])

        if rp == 5:
            if rd == 0:  # dado 1
                piezaa = np.array([[1, 1, 1, 1], [0, 0, 1, 0]])
                piezab = np.array([[1], [1]])
                piezac = np.array([[1, 1, 0], [1, 1, 1]])
                piezad = np.array([[1, 0], [1, 1], [1, 0]])
            if rd == 1:  # dado 2
                piezaa = np.array([[1, 0], [1, 1], [1, 0]])
                piezab = np.array([[0, 0, 0, 1], [1, 1, 1, 1]])
                piezac = np.array([[1], [1]])
                piezad = np.array([[1, 1, 0], [1, 1, 1]])
            if rd == 2:  # dado 3
                piezaa = np.array([[1], [1]])
                piezab = np.array([[1, 1, 0], [1, 1, 1]])
                piezac = np.array([[1, 1, 1, 1], [0, 0, 1, 0]])
                piezad = np.array([[0, 1], [1, 1], [1, 0]])
            if rd == 3:  # dado 4
                piezaa = np.array([[1, 1, 1]])
                piezab = np.array([[1, 1], [1, 1]])
                piezac = np.array([[1, 0], [1, 0], [1, 1]])
                piezad = np.array([[0, 1], [1, 1]])
            if rd == 4:  # dado 5
                piezaa = np.array([[0, 1], [1, 1], [1, 0]])
                piezab = np.array([[1, 1, 0], [1, 1, 1]])
                piezac = np.array([[1, 0], [1, 0], [1, 1]])
                piezad = np.array([[0, 1], [1, 1]])
            if rd == 5:  # dado 6
                piezaa = np.array([[1, 0], [1, 0], [1, 1]])
                piezab = np.array([[1, 1, 1]])
                piezac = np.array([[1, 1], [1, 1]])
                piezad = np.array([[1, 1, 0], [1, 1, 1]])

        piezas = [piezaa, piezab, piezac]
        return piezas

    def generar_estadistica(self):
        pass

    def dibujar(self):
        pass
