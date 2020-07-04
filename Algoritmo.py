import numpy as np


def crearPieza(x, y, pieza, num_rows, num_cols, i):
    num_rowsP, num_colsP = pieza.shape
    # print("numcols,numrows",num_cols, num_rows)
    p = np.zeros((num_cols, num_rows))
    p[x:x + num_rowsP, y:y + num_colsP] = pieza * (i + 1)
    return p


def encajar(matA, matB):
    return matA + matB


def la_pieza_Encaja(sumaplantilla, i):
    for x in sumaplantilla:
        for y in x:
            if y == 100:
                pass
            elif y > i + 1:
                return False
    return True


iteracion = 0
intentos = []


def probarPiezarec(x, y, piezas, plantilla, i, rotar, nrot):
    # print("nrot",nrot)
    # time.sleep(1)
    global iteracion
    iteracion += 1
    global intentos

    num_rows, num_cols = plantilla.shape

    if rotar:
        piezas[i] = np.rot90(piezas[i])
        # print(piezas[i])

    num_rowsP, num_colsP = piezas[i].shape
    # print(num_rowsP, num_colsP)
    pieza = piezas[i]
    # print(piezas[i])
    piezaM = crearPieza(x, y, pieza, num_cols, num_rows, i)

    sumaplantilla = piezaM + plantilla

    # print(sumaplantilla)

    if la_pieza_Encaja(sumaplantilla, i):
        intentos.append(sumaplantilla)
        # print(sumaplantilla)
        if i < len(piezas) - 1:
            if probarPiezarec(0, 0, piezas, sumaplantilla, i + 1, False, 0):

                # return probarPiezarec(0,0,piezas,sumaplantilla,i+1)
                # else:
                return True
            else:

                # print('x=',num_rows , num_rowsP,i)
                if y < num_cols - num_colsP:
                    return probarPiezarec(x, y + 1, piezas, plantilla, i, rotar, nrot)
                # print('y=',num_cols,num_colsP,i)
                if x < num_rows - num_rowsP:
                    return probarPiezarec(x + 1, 0, piezas, plantilla, i, rotar, nrot)
                if nrot == 4:
                    return False
                if rotar:
                    pass
                else:
                    return probarPiezarec(0, 0, piezas, plantilla, i, True, nrot + 1)
        else:
            return True
    else:
        # print('x=',num_rows , num_rowsP,i)
        if y < num_cols - num_colsP:
            return probarPiezarec(x, y + 1, piezas, plantilla, i, False, nrot)
        # print('y=',num_cols,num_colsP,i)
        if x < num_rows - num_rowsP:
            return probarPiezarec(x + 1, 0, piezas, plantilla, i, False, nrot)
        if nrot == 4:
            return False
        if rotar:
            pass
        else:
            return probarPiezarec(0, 0, piezas, plantilla, i, True, nrot + 1)

    return False

'''
plantilla = np.array([[0, 0, 0, 0], [0, 0, 100, 100], [0, 0, 100, 100], [0, 0, 0, 0], [0, 0, 0, 0], [100, 100, 100, 0]])
plantilla_simple = np.array([[0, 0, 0, 0, 100], [100, 0, 0, 0, 100], [100, 0, 0, 0, 0], [100, 100, 0, 0, 100]])
piezaSimple1 = np.array([[1, 1]])
piezaSimple2 = np.array([[1, 1, 1],
                         [0, 0, 1]])
piezasSimples = [piezaSimple1, piezaSimple2]

piezaa = np.array([[1, 1],
                   [0, 1],
                   [0, 1]])
piezab = np.array([[1, 0, 0, 0],
                   [1, 1, 1, 1]])
piezac = np.array([[1, 0],
                   [1, 1],
                   [1, 0]])

piezad = np.array([[1, 1], [0, 1], [0, 1]])
piezas = [piezaa, piezab, piezac]

pieza = np.array([[0, 1], [1, 1]])
pieza2 = np.array([[1], [1]])
pieza3 = np.array([[1, 1, 1]])
pieza4 = np.array([[1]])
pieza5 = np.array([[1, 0], [1, 0]])
# piezax = np.array([[1],[1]])
# piezay = np.array([[1,1],[1,0]])
# piezaz = np.array([[0,0,1],[1,1,1]])
piezax = np.array([[1, 1], [1, 0]])
piezay = np.array([[0, 1], [1, 1]])
piezaz = np.array([[1], [1], [1]])
'''

# piezas = np.array([pieza,pieza3])
# piezas = [pieza,pieza2,pieza3,pieza4]
# piezas = [piezax,piezay,piezaz]

# probarPieza(0,0,pieza,plantilla)
def resolverPuzzle(piezas, plantilla):
    probarPiezarec(0, 0, piezas, plantilla, 0, False, 0)
    return intentos


# piezas.shape[0]

#print("Cantidad de iteraciones: ", iteracion)
