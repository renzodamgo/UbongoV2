import random
import numpy as np


class Mazo:
    def __init__(self):
        pass

    def dar_cartilla(self):
        # valplantilla = (random.randrange(0,6))
        valplantilla = 3
        if valplantilla == 0:
            plantilla = np.array([[0, 0, 0, 0, 100], [100, 0, 0, 0, 100], [100, 0, 0, 0, 0], [100, 100, 0, 0, 100]])

        elif valplantilla == 1:
            plantilla = np.array([[0, 0, 0, 100, 100], [0, 0, 0, 0, 100], [0, 0, 0, 0, 0], [0, 100, 100, 100, 100]])

        elif valplantilla == 2:
            plantilla = np.array([[0, 0, 0, 100, 100], [100, 0, 0, 100, 100], [100, 0, 0, 0, 0], [100, 0, 0, 0, 0]])

        elif valplantilla == 3:
            plantilla = np.array(
                [[100, 100, 0, 100], [100, 100, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [100, 0, 0, 0], [100, 0, 0, 0]])

        elif valplantilla == 4:
            plantilla = np.array(
                [[100, 100, 0, 0, 100], [100, 100, 0, 0, 100], [100, 100, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

        elif valplantilla == 5:
            plantilla = np.array([[100, 0, 0, 0, 0], [100, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 100, 0, 100]])
        return plantilla, valplantilla


