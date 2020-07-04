import random
import numpy as np


class Mazo:
    def __init__(self, plantillas):
        self.plantillas = plantillas

    def dar_cartilla(self):
        valplantilla = (random.randrange(5))
        if valplantilla == 0:
            plantilla1 = np.array([[0, 0, 0, 0, 100], [100, 0, 0, 0, 100], [100, 0, 0, 0, 0], [100, 100, 0, 0, 100]])
            return plantilla1, valplantilla
        elif valplantilla == 1:
            plantilla2 = np.array([[0, 0, 0, 100, 100], [0, 0, 0, 0, 100], [0, 0, 0, 0, 0], [0, 100, 100, 100, 100]])
            return plantilla2, valplantilla
        elif valplantilla == 2:
            plantilla3 = np.array([[0, 0, 0, 100, 100], [100, 0, 0, 100, 100], [100, 0, 0, 0, 0], [100, 0, 0, 0, 0]])
            return plantilla3, valplantilla
        elif valplantilla == 3:
            plantilla4 = np.array(
                [[100, 100, 0, 100], [100, 100, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [100, 0, 0, 0], [100, 0, 0, 0]])
            return plantilla4, valplantilla
        elif valplantilla == 4:
            plantilla5 = np.array(
                [[100, 100, 0, 0, 100], [100, 100, 0, 0, 100], [100, 100, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
            return plantilla5, valplantilla

    