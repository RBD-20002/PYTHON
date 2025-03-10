# Los conjuntos son una estructura de datos que permite almacenar elementos de forma desordenada.
# Se crean con llaves y los elementos se separan por comas.
# Los conjuntos son mutables, es decir, se pueden modificar una vez creados.
# Los conjuntos no permiten elementos duplicados.
# Los conjuntos no permiten elementos nulos.
# Los conjuntos no permiten elementos vacíos.
# Los conjuntos no permiten elementos mutables.
# Los conjuntos pueden contener cualquier tipo de dato.
# Los conjuntos pueden contener tuplas.
# Los conjuntos no pueden contener listas.
# Los conjuntos no pueden contener diccionarios.
# Los conjuntos no pueden contener otros conjuntos.
# Los conjuntos pueden contener cualquier combinación de los tipos de datos anteriores, siempre que estos sean inmutables.

# Crear un conjunto vacío
conjunto_vacio = set()
print(conjunto_vacio)

print("-"*80)

# Crear un conjunto con elementos
conjunto = {1, 2, 3, 4, 5, 5, 5}
print(conjunto)

print("-"*80)

# Crear un conjunto con elementos de diferentes tipos
conjunto_tipos = {1, 'hola', 3.14, True, False, 0, -5}
print(conjunto_tipos)

print("-"*80)

# Crear un conjunto con listas
# conjunto_listas = {[1, 2], [3, 4], [5, 6]} # Error: type list is unhashable
# print(conjunto_listas)

print("-"*80)

# Crear un conjunto con tuplas
conjunto_tuplas = {(1, 2), (3, 4), (5, 6)}
print(conjunto_tuplas)

print("-"*80)

# Crear un conjunto con diccionarios
# conjunto_diccionarios = {{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}} # Error: type dict is unhashable
# print(conjunto_diccionarios)

print("-"*80)

# Crear un conjunto con otros conjuntos
# conjunto_conjuntos = {{1, 2}, {3, 4}, {5, 6}} # Error: type set is unhashable
# print(conjunto_conjuntos)

print("-"*80)

# Acceso a los elementos de un conjunto
conjunto = {1, 2, 3, 4, 5}

# Los conjuntos no permiten acceder a los elementos por índice
# print(conjunto[0]) # Error

print("-"*80)

# Añadir elementos a un conjunto
conjunto.add(6)
print(conjunto)

print("-"*80)

# Eliminar elementos de un conjunto
conjunto.remove(6)
print(conjunto)

print("-"*80)

# Comprobar si un elemento está en un conjunto
print(1 in conjunto)
print(6 in conjunto)

print("-"*80)

# Longitud de un conjunto
print(len(conjunto))

print("-"*80)

# Vaciar un conjunto
conjunto.clear()

print("-"*80)

# Comprobar si un conjunto está vacío
print(len(conjunto) == 0)

print("<-------------------OPERACIONES CON CONJUNTOS---------------->")

# Operaciones con conjuntos
# Unión de conjuntos
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

union = conjunto1.union(conjunto2)
print(union)

print("-"*80)

# Intersección de conjuntos
interseccion = conjunto1.intersection(conjunto2)
print(interseccion)

print("-"*80)

# Diferencia de conjuntos
diferencia = conjunto1.difference(conjunto2)
print(diferencia)

print("-"*80)

# Diferencia simétrica de conjuntos
diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
print(diferencia_simetrica)

print("-"*80)

# Comprobar si un conjunto es subconjunto de otro
print(conjunto1.issubset(conjunto2))
print(conjunto1.issubset({1, 2, 3, 4, 5, 6, 7, 8}))

print("-"*80)

# Comprobar si un conjunto es superconjunto de otro
print(conjunto1.issuperset(conjunto2))
print(conjunto1.issuperset({1, 2, 3, 4, 5}))

print("-"*80)

# Comprobar si dos conjuntos son disjuntos
print(conjunto1.isdisjoint(conjunto2))
print(conjunto1.isdisjoint({6, 7, 8, 9, 10}))

print("-"*80)

# Copiar un conjunto
conjunto_copia = conjunto1.copy()
print(conjunto_copia)

print("-"*80)

# Iterar sobre un conjunto
for elemento in conjunto1:
    print(elemento)

