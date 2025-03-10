"""Intermedio: Matrices, diccionarios y tuplas"""

"""Crea una matriz 3x3 y almacena la suma de cada fila en un diccionario, donde las claves sean tuplas con los índices de cada fila."""
entrada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#    Salida esperada: {(0,): 6, (1,): 15, (2,): 24}

print("-----------------------------------------------------------------")

"""Dado un diccionario que asocia números con tuplas de coordenadas, crea una matriz de ceros y llena las posiciones indicadas por las tuplas con los números correspondientes."""
entrada = {1: (0, 0), 2: (1, 1), 3: (2, 2)}
#    Salida esperada: [[1, 0, 0], [0, 2, 0], [0, 0, 3]]

print("-----------------------------------------------------------------")

"""Genera una matriz de 4x4 con números aleatorios entre 1 y 10, luego guarda en un diccionario cuántas veces aparece cada número."""
entrada = [[1, 2], [2, 3], [3, 4], [4, 5]]
#    Salida esperada: {1: 1, 2: 2, 3: 2, 4: 2, 5: 1}

print("-----------------------------------------------------------------")

"""Convierte una matriz 2x3 en un diccionario donde las claves sean tuplas de índices (i, j) y los valores sean los elementos de la matriz."""
entrada = [[5, 6], [7, 8], [9, 10]]
#    Salida esperada: {(0, 0): 5, (0, 1): 6, (1, 0): 7, (1, 1): 8, (2, 0): 9, (2, 1): 10}


"""Avanzado: Matrices, diccionarios y conjuntos"""

"""Crea una matriz 5x5 y llena un conjunto con los elementos únicos de la matriz."""
entrada = [[1, 2], [2, 3], [3, 1], [1, 2]]
#    Salida esperada: {1, 2, 3}

print("-----------------------------------------------------------------")

"""Genera una matriz aleatoria 3x3 y crea un diccionario que relacione cada valor único con su posición (en forma de conjunto de tuplas)."""
entrada = [[1, 1, 2], [3, 3, 3], [2, 2, 2]]
#    Salida esperada: {1: {(0, 0), (0, 1)}, 2: {(0, 2), (2, 0), (2, 1), (2, 2)}, 3: {(1, 0), (1, 1), (1, 2)}}

print("-----------------------------------------------------------------")

"""Llena una matriz 4x4 con números aleatorios entre 1 y 5 y elimina los duplicados utilizando conjuntos."""
entrada = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
#    Salida esperada: {1}

print("-----------------------------------------------------------------")

"""Convierte una matriz 2x3 en un conjunto con todos sus elementos únicos y muestra cuántos elementos únicos contiene."""
entrada = [[1, 2, 3], [4, 5, 6]]
#    Salida esperada: 3