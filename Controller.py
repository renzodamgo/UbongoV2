import random as rand
import numpy as np
import Player
import random
import Mazo

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
        self.Mazo = Mazo.Mazo()

    def mover(self, dir):
        self.Jugadores[0].mover(dir)

    def play(self):
        pass

    def elegir_pos(self, pos):
        return self.posC

    def roll_dice(self):
        return rand.randrange(0, 5)

    def asignar_piezas(self, rd, rp):
        if rp == 0:
            if rd == 0:  # dado 1
                piezaa = np.array([[0, 0, 1],
                                   [1, 1, 1],
                                   [1, 0, 0]])
                piezab = np.array([[1, 1, 1],
                                   [1, 1, 0]])
                piezac = np.array([[1, 1, 1]])
            if rd == 1:  # dado 2
                piezaa = np.array([[0, 1], [1, 1], [1, 0]])
                piezab = np.array([[1, 1, 1], [0, 1, 1]])
                piezac = np.array([[1, 0], [1, 0], [1, 1]])
            if rd == 2:  # dado 3
                piezaa = np.array([[1, 1], [0, 1], [0, 1]])
                piezab = np.array([[1, 0, 0, 0], [1, 1, 1, 1]])
                piezac = np.array([[1, 0], [1, 1], [1, 0]])
            if rd == 3:  # dado 4
                piezaa = np.array([[1, 1], [0, 1]])
                piezab = np.array([[0, 0, 1, 0], [1, 1, 1, 1]])
                piezac = np.array([[1, 1, 1], [0, 1, 1]])
            if rd == 4:  # dado 5
                piezaa = np.array([[1, 1, 1, 1]])
                piezab = np.array([[0, 1, 1], [1, 1, 0]])
                piezac = np.array([[1, 1, 1], [1, 1, 0]])
            if rd == 5:  # dado 6
                piezaa = np.array([[0, 1, 1], [1, 1, 0]])
                piezab = np.array([[1, 1], [1, 1]])
                piezac = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 0]])
            piezas = [piezaa, piezab, piezac]

        if rp == 1:
            if rd == 0:  # dado 1
                piezaa = np.array([[1, 1, 1, 1]])
                piezab = np.array([[1, 1, 0], [1, 1, 1]])
                piezac = np.array([[1, 0], [1, 1], [1, 0]])
            if rd == 1:  # dado 2
                piezaa = np.array([[1, 1, 1], [0, 0, 1]])
                piezab = np.array([[1, 0], [1, 1], [1, 0]])
                piezac = np.array([[1, 1, 0], [1, 1, 1]])
            if rd == 2:  # dado 3
                piezaa = np.array([[1, 1, 1, 1], [0, 0, 1, 0]])
                piezab = np.array([[0, 1], [1, 1], [1, 0]])
                piezac = np.array([[1, 1, 1, 1]])
            if rd == 3:  # dado 4
                piezaa = np.array([[1, 1, 1]])
                piezab = np.array([[1, 1, 0], [1, 1, 1]])
                piezac = np.array([[0, 0, 1, 0], [1, 1, 1, 1]])
            if rd == 4:  # dado 5
                piezaa = np.array([[1, 1], [1, 0], [1, 0]])
                piezab = np.array([[1, 1, 1, 1]])
                piezac = np.array([[1, 1, 0], [1, 1, 1]])
            if rd == 5:  # dado 6
                piezaa = np.array([[0, 1], [1, 1], [1, 0]])
                piezab = np.array([[1, 0], [1, 0], [1, 1]])
                piezac = np.array([[1, 1, 1], [1, 1, 0]])
            piezas = [piezaa, piezab, piezac]

        if rp == 2:
            if rd == 0:  # dado 1
                piezaa = np.array([[0, 1], [0, 1], [1, 1]])
                piezab = np.array([[0, 1, 1], [1, 1, 1]])
                piezac = np.array([[1, 0], [1, 1], [1, 0]])
            if rd == 1:  # dado 2
                piezaa = np.array([[0, 1], [1, 1], [1, 0]])
                piezab = np.array([[1, 0], [1, 1], [1, 0]])
                piezac = np.array([[0, 1, 1], [1, 1, 1]])
            if rd == 2:  # dado 3
                piezaa = np.array([[1, 0], [1, 1], [1, 0]])
                piezab = np.array([[0, 1], [0, 1], [1, 1]])
                piezac = np.array([[1, 0, 0], [1, 1, 1], [0, 0, 1]])
            if rd == 3:  # dado 4
                piezaa = np.array([[1, 0], [1, 0], [1, 1]])
                piezab = np.array([[1, 0, 0, 0], [1, 1, 1, 1]])
                piezac = np.array([[1, 1, 1, 1]])
            if rd == 4:  # dado 5
                piezaa = np.array([[0, 1], [1, 1]])
                piezab = np.array([[1, 1, 1, 1], [0, 1, 0, 0]])
                piezac = np.array([[0, 0, 0, 1], [1, 1, 1, 1]])
            if rd == 5:  # dado 6
                piezaa = np.array([[1, 1, 1, 1], [0, 0, 0, 1]])
                piezab = np.array([[1, 1], [1, 1]])
                piezac = np.array([[1, 0], [1, 0], [1, 1]])
            piezas = [piezaa, piezab, piezac]
        if rp == 3:
            if rd == 0:  # dado 1
                piezaa = np.array([[1, 0], [1, 1], [1, 0]])
                piezab = np.array([[0, 1], [1, 1], [1, 0]])
                piezac = np.array([[1, 1], [1, 1]])
                piezad = np.array([[1, 0, 0, 0], [1, 1, 1, 1]])
            if rd == 1:  # dado 2
                piezaa = np.array([[1, 1, 1]])
                piezab = np.array([[1, 1, 1, 1], [0, 0, 1, 0]])
                piezac = np.array([[1, 1, 1], [1, 1, 0]])
                piezad = np.array([[1, 0], [1, 1], [1, 0]])
            if rd == 2:  # dado 3
                piezaa = np.array([[1, 0], [1, 1], [1, 0]])
                piezab = np.array([[0, 1, 1], [1, 1, 1]])
                piezac = np.array([[0, 1], [1, 1]])
                piezad = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 0]])
            if rd == 3:  # dado 4
                piezaa = np.array([[1, 0], [1, 1], [0, 1]])
                piezab = np.array([[1, 1, 1, 1], [0, 0, 1, 0]])
                piezac = np.array([[1, 1, 1]])
                piezad = np.array([[1, 0, 0, 0], [1, 1, 1, 1]])
            if rd == 4:  # dado 5
                piezaa = np.array([[1, 0], [1, 0], [1, 1]])
                piezab = np.array([[1, 1, 1], [1, 1, 0]])
                piezac = np.array([[1, 1, 1, 1], [0, 1, 0, 0]])
                piezad = np.array([[0, 1], [1, 1]])
            if rd == 5:  # dado 6
                piezaa = np.array([[0, 1], [1, 1], [1, 0]])
                piezab = np.array([[0, 1], [0, 1], [1, 1]])
                piezac = np.array([[1, 1, 1], [1, 1, 0]])
                piezad = np.array([[1, 1], [1, 1]])
            piezas = [piezaa, piezab, piezac, piezad]

        if rp == 4:
            if rd == 0:  # dado 1
                piezaa = np.array([[1, 0, 0, 0], [1, 1, 1, 1]])
                piezab = np.array([[0, 1, 0], [1, 1, 1]])
                piezac = np.array([[1], [1], [1]])
                piezad = np.array([[1, 1], [1, 1], [0, 1]])
            if rd == 1:  # dado 2
                piezaa = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 0]])
                piezab = np.array([[1, 1, 1], [1, 1, 0]])
                piezac = np.array([[1], [1]])
                piezad = np.array([[0, 0, 1, 0], [1, 1, 1, 1]])
            if rd == 2:  # dado 3
                piezaa = np.array([[1, 1], [1, 1]])
                piezab = np.array([[0, 0, 1, 0], [1, 1, 1, 1]])
                piezac = np.array([[1, 1, 0], [1, 1, 1]])
                piezad = np.array([[1, 0], [1, 0], [1, 1]])
            if rd == 3:  # dado 4
                piezaa = np.array([[1, 0], [1, 1], [1, 0]])
                piezab = np.array([[1, 1, 1, 1]])
                piezac = np.array([[0, 1], [1, 1], [1, 0]])
                piezad = np.array([[1, 1], [1, 1]])
            if rd == 4:  # dado 5
                piezaa = np.array([[1, 1], [1, 1]])
                piezab = np.array([[1, 1, 1, 1], [0, 0, 0, 1]])
                piezac = np.array([[1, 0], [1, 1], [0, 1]])
                piezad = np.array([[1, 1], [1, 1]])
            if rd == 5:  # dado 6
                piezaa = np.array([[1, 1], [1, 0], [1, 0]])
                piezab = np.array([[1, 0], [1, 1], [0, 1]])
                piezac = np.array([[1, 1, 0], [1, 1, 1]])
                piezad = np.array([[1, 1], [1, 1]])
            piezas = [piezaa, piezab, piezac, piezad]

        if rp == 5:
            if rd == 0:  # dado 1
                piezaa = np.array([[1, 1, 1, 1], [0, 0, 1, 0]])
                piezab = np.array([[1], [1]])
                piezac = np.array([[1, 1, 0], [1, 1, 1]])
                piezad = np.array([[1, 0], [1, 1], [1, 0]])
            if rd == 1:  # dado 2
                piezaa = np.array([[1, 0], [1, 1], [1, 0]])
                piezab = np.array([[1, 1, 1, 1], [0, 0, 0, 1]])
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
                piezac = np.array([[1, 0], [1, 1], [0, 1]])
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
                piezad = np.array([[0, 1, 1], [1, 1, 1]])

            piezas = [piezaa, piezab, piezac,piezad]
        return piezas

    def generar_estadistica(self):
        pass

    def dibujar(self, screen, _intentos, _puzzles):

        posx_ini = 0
        x = posx_ini
        y = 100
        posy_ini = 100
        n = 0
        for i in _intentos:

            x = posx_ini
            for rows in i:
                for cols in rows:
                    if cols == 0:
                        screen.blit(_puzzles[5], (x, y))
                    elif cols == 100:
                        screen.blit(_puzzles[6], (x, y))
                    else:
                        screen.blit(_puzzles[int(cols)], (x, y))
                    x += 30
                y += 30
                x = posx_ini
            y += 50

            n += 1
            if n % 4 == 0:
                posx_ini += 250
                y = posy_ini
