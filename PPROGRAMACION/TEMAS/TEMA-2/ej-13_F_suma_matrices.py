def matrices_simetrica(matrizA,matrizB):
    if len(matrizA) != len(matrizB):
        return False
    for i in range(len(matrizA)):
        if len(matrizA[i]) != len(matrizB[i]):
            return False
    return True

def suma_matrices(matrizA,matrizB):
    if not matrices_simetrica(matrizA,matrizB):
        return None
    matriz_suma = []
    for i in range(len(matrizA)):
        fila = []
        for j in range(len(matrizA[i])):
            fila.append(matrizA[i][j]+matrizB[i][j])
        matriz_suma.append(fila)
    return matriz_suma