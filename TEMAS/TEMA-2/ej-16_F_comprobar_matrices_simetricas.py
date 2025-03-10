"""
def matrices_cuadrada(matrizA,matrizB):
    if len(matrizA) != len(matrizB):
        return False
    for i in range(len(matrizA)):
        if len(matrizA[i]) != len(matrizB[i]):
            return False
    return True
"""

def matriz_cuadrada():
    filas = len(matriz)
    for fial in matrix:
        if len(matrix) != filas:
            return False
    return True


def matriz_simetrica():
    if not matriz_cuadrada(matriz):
        return None
    simetrica = []
    for i in range(len(matriz)):
        simetrica.append([])
        for j in range(len(matriz)):
            simetrica[i].append(matriz[j][i])
    return simetrica

def esSimetrica():
    if not matriz_cuadrada():
        return False
    return matriz == matriz_simetrica(matriz)