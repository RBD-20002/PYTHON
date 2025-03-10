# Los diccionarios no permiten claves duplicadas.
# Los diccionarios no permiten claves nulas.
# Los diccionarios no permiten claves vacías.

# Crear un diccionario vacío
diccionario_vacio = {}
print(diccionario_vacio)

print("-"*80)

# Crear un diccionario con un solo elemento
diccionario_un_elemento = {'a': 1}
print(diccionario_un_elemento)

print("-"*80)

# Crear un diccionario con varios elementos
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(diccionario)

print("-"*80)

# Crear un diccionario con claves de diferentes tipos
diccionario_tipos = {1: 'uno', 'dos': 2, 3.0: 'tres', True: 'cuatro', False: 'cinco', 0: 'seis'}
print(diccionario_tipos)

print("-"*80)

# Crear un diccionario con diccionarios
diccionario_diccionarios = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}, 'g': {'h': 5, 'i': 6}}
print(diccionario_diccionarios)

print("-"*80)

# Crear un diccionario con listas
diccionario_listas = {'a': [1, 2], 'b': [3, 4], 'c': [5, 6]}
print(diccionario_listas)

print("-"*80)

# Crear un diccionario con tuplas
diccionario_tuplas = {'a': (1, 2), 'b': (3, 4), 'c': (5, 6)}
print(diccionario_tuplas)

print("-"*80)

# Crear un diccionario con conjuntos
diccionario_conjuntos = {'a': {1, 2}, 'b': {3, 4}, 'c': {5, 6}}
print(diccionario_conjuntos)

print("-"*80)

# Acceso a los elementos de un diccionario
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print("-"*80)

# Acceder al valor de una clave
print(diccionario['a'])

print("-"*80)

# Modificar el valor de una clave
diccionario['a'] = 10
print(diccionario)

print("-"*80)

# Añadir un nuevo elemento al diccionario
diccionario['f'] = 6
print(diccionario)

print("-"*80)

# Eliminar un elemento del diccionario
del diccionario['f']
print(diccionario)

print("-"*80)

# Comprobar si una clave existe en el diccionario
print('a' in diccionario)
print('f' in diccionario)

print("-"*80)

# Comprobar si una clave no existe en el diccionario
print('a' not in diccionario)
print('f' not in diccionario)

print("-"*80)

# Acceder a un elemento que no existe en el diccionario
try:
    print(diccionario['f'])
except KeyError as e:
    print(e)

print("-"*80)

# Acceder a un elemento que no existe en el diccionario con get
print(diccionario.get('f'))

print("-"*80)

# Acceder a un elemento que no existe en el diccionario con get y un valor por defecto
print(diccionario.get('f', 'No existe')) # No existe

print("-"*80)

# Acceder a un elemento que no existe en el diccionario con setdefault
print(diccionario.setdefault('f', 6)) 

print("-"*80)

# Devuelve el valor por defecto si la clave no existe y lo añade al diccionario
print(diccionario) # {'a': 10, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

print("-"*80)

# El método update permite añadir varios elementos a la vez
diccionario.update({'g': 7, 'h': 8, 'i': 9})
print(diccionario)

print("-"*80)

# El método pop permite eliminar un elemento del diccionario
print(diccionario.pop('g'))

print("-"*80)

# El método popitem permite eliminar el último elemento del diccionario
print(diccionario.popitem())

print("-"*80)

# El método clear permite eliminar todos los elementos del diccionario
diccionario.clear()
print(diccionario)

print("-"*80)

# El método keys permite obtener las claves del diccionario
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(diccionario.keys())

print("-"*80)

# El método values permite obtener los valores del diccionario
print(diccionario.values())

print("-"*80)

# El método items permite obtener los elementos del diccionario
print(diccionario.items())

print("-"*80)

# El método copy permite copiar un diccionario
diccionario_copia = diccionario.copy()
print(diccionario_copia)

print("-"*80)

# El método fromkeys permite crear un diccionario a partir de una lista de claves
claves = ['a', 'b', 'c', 'd', 'e']
diccionario = dict.fromkeys(claves)
print(diccionario)

print("-"*80)

# El método fromkeys permite crear un diccionario a partir de una lista de claves con un valor por defecto
diccionario = dict.fromkeys(claves, 0)
print(diccionario)

print("-"*80)

# Recorrer un diccionario con un bucle for
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
for clave in diccionario:
    print(clave, diccionario[clave])
print("--------------")

print("-"*80)

# Recorrer un diccionario con un bucle for y el método items
for clave, valor in diccionario.items():
    print(clave, valor)
print("--------------")

print("-"*80)

# Recorrer un diccionario con un bucle for y el método keys
for clave in diccionario.keys():
    print(clave, diccionario[clave])
print("--------------")

print("-"*80)

# Recorrer un diccionario con un bucle for y el método values
for valor in diccionario.values():
    print(valor)
print("--------------")

print("-"*80)

# Recorrer un diccionario con un bucle while
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
claves = list(diccionario.keys())
i = 0
while i < len(claves):
    clave = claves[i]
    print(clave, diccionario[clave])
    i += 1
