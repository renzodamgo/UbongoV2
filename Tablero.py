import numpy as np


class Tablero:
    def __init__(self):
        self.tablero = x = np.random.choice([1, 2, 3, 4], size=(6, 6))
        self.posX = [0, 0, 0, 0, 0, 0]

    def coger_gemas(self, posY):
        gemas = self.tablero[posY, self.posX[posY]:self.posX[posY] + 2]

        self.tablero[posY, self.posX[posY]:self.posX[posY] + 2] = [0, 0]
        self.posX[posY] = self.posX[posY] + 2
        return gemas



