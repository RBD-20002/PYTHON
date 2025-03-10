
matriz1 = [[1, 2, 3], [4, 5, 6]]
matriz2 = [[7, 8, 9], [10, 11, 12]]

print("--------------------------------SUMA")
def suma_matrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    resultado = []

    for i in range(filas):
        fila_resultado = []
        for j in range(columnas):
            fila_resultado.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(fila_resultado)
    return resultado

print(suma_matrices(matriz1,matriz2))

print("--------------------------------RESTA")
def resta_matrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    resultado = []

    for i in range(filas):
        fila_resultado = []
        for j in range(columnas):
            fila_resultado.append(matriz1[i][j] - matriz2[i][j])
        resultado.append(fila_resultado)
    return resultado

print(resta_matrices(matriz1,matriz2))

print("--------------------------------MULTIPLICACION")
def multiplicacion_matrices(matriz1, matriz2):
    filas_matriz1 = len(matriz1)
    columnas_matriz1 = len(matriz1[0])
    filas_matriz2 = len(matriz2)
    columnas_matriz2 = len(matriz2[0])
    if columnas_matriz1 != filas_matriz2:
        return None  # No se pueden multiplicar si no cumplen la condición
    resultado = []
    for i in range(filas_matriz1):
        fila_resultado = []
        for j in range(columnas_matriz2):
            valor = 0
            for k in range(columnas_matriz1):
                valor += matriz1[i][k] * matriz2[k][j]
            fila_resultado.append(valor)
        resultado.append(fila_resultado)
    return resultado

print(multiplicacion_matrices(matriz1,matriz2))

print("--------------------------------TRASPUESTA")
def transpuesta(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    resultado = []
    for j in range(columnas):
        fila_resultado = []
        for i in range(filas):
            fila_resultado.append(matriz[i][j])
        resultado.append(fila_resultado)
    return resultado

print(transpuesta(matriz1))

print("--------------------------------MULTIPLICACION ESCALAR")
def multiplicacion_escalar(matriz, escalar):
    filas = len(matriz)
    columnas = len(matriz[0])
    resultado = []
    for i in range(filas):
        fila_resultado = []
        for j in range(columnas):
            fila_resultado.append(matriz[i][j] * escalar)
        resultado.append(fila_resultado)
    return resultado

print(multiplicacion_escalar(matriz1,2))

print("--------------------------------DIAGONAL")
def diagonal(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    diagonal_resultado = []
    for i in range(min(filas, columnas)):
        diagonal_resultado.append(matriz[i][i])
    return diagonal_resultado

print(diagonal(matriz1))

print("--------------------------------ROTACION 90º")
def rotacion_90(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    resultado = []
    for j in range(columnas):
        fila_resultado = []
        for i in range(filas - 1, -1, -1):
            fila_resultado.append(matriz[i][j])
        resultado.append(fila_resultado)
    return resultado

print(rotacion_90(matriz1))

print("--------------------------------SIMETRICA")
def es_simetrica(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    if filas != columnas:  # Una matriz simétrica debe ser cuadrada
        return False
    for i in range(filas):
        for j in range(i, columnas):  # Solo verificar la mitad superior
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

matriz_simetrica = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
print(es_simetrica(matriz_simetrica))

print("--------------------------------SUMA FILA Y COLUMNA")
def suma_filas(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    suma_filas_resultado = []
    for i in range(filas):
        suma_filas_resultado.append(sum(matriz[i]))
    return suma_filas_resultado

print(suma_filas(matriz1))

def suma_columnas(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    suma_columnas_resultado = []
    for j in range(columnas):
        suma_columna = 0
        for i in range(filas):
            suma_columna += matriz[i][j]
        suma_columnas_resultado.append(suma_columna)
    return suma_columnas_resultado

print(suma_columnas(matriz2))

print("--------------------------------DECTECCION DUPLICADOS Y UNICOS")
def elementos_unicos(matriz):
    elementos = []
    for fila in matriz:
        for elemento in fila:
            if elemento not in elementos:
                elementos.append(elemento)
    return elementos

def elementos_duplicados(matriz):
    elementos = []
    duplicados = []
    for fila in matriz:
        for elemento in fila:
            if elemento in elementos and elemento not in duplicados:
                duplicados.append(elemento)
            else:
                elementos.append(elemento)
    return duplicados

matriz_con_duplicados = [[1, 2, 2], [3, 4, 4], [5, 1, 6]]
print(elementos_unicos(matriz_con_duplicados))
print(elementos_duplicados(matriz_con_duplicados))

print("--------------------------------MATRICES DE CERO")
def matriz_ceros(filas: int, columnas: int) -> list:
    if filas == 0:
        return []
    return [[0] * columnas] + matriz_ceros(filas - 1, columnas)

print(matriz_ceros(5,5))

print("--------------------------------DIBUJAR UNA MATRIZ")

def dibujar_matriz(matriz):
    if not matriz:  
        print("La matriz está vacía.")
        return
    longitud_fila = len(matriz[0])
    for fila in matriz:
        if len(fila) != longitud_fila:
            print("Error: Todas las filas de la matriz deben tener la misma cantidad de elementos.")
            return
    for fila in matriz:
        print(" | ".join(map(str, fila)))  
    print()  

matriz1 = [[1, 2, 3], [4, 5, 6]]
matriz2 = [[7, 8, 9], [10, 11]]  
print("Matriz 1:")
dibujar_matriz(matriz1)

print("Matriz 2:")
dibujar_matriz(matriz2)