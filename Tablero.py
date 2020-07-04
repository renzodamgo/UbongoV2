import numpy as np


class Tablero:
    def __init__(self):
        self.tablero = x = np.random.choice([1, 2, 3, 4], size=(6, 12))

    def coger_gemas(self, posY, posX):
        return self.tablero[posY, posX + 1:posX + 3]

