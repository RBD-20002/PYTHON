def multiplicar_matrice(matrizA,matrizB):
    if len(matrizA[0]) != len(matrizB):
        return None
    matriz_resultado = []
    for i in range(matrizA):
        fila = []
        for j in range(matrizB[0]):
            producto = 0
            for k in range(len(matrizA[i])):
                producto += matrizA[i][k] * matrizB[k][j]
            fila.append(producto)
        matriz_resultado.append(fila)
    return matriz_resultado