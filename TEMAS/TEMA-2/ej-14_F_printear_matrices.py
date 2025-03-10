def imagen_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end= "\t")
        print()

if __name__ == "__main__":
    matriz = [[1,2,3],[4,5,6],[7,8,9]]
    imagen_matriz(matriz)