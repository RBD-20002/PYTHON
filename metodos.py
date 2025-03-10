# Métodos y funciones de Python comunes:

len()
# Descripción: Devuelve la longitud (el número de elementos) de un objeto como una cadena, lista, tupla, diccionario, etc.
# Ejemplo: len("Hola") devuelve 4.

str()
# Descripción: Convierte un valor en una cadena de texto (string).
# Ejemplo: str(123) devuelve "123".

int()
# Descripción: Convierte un valor en un número entero.
# Ejemplo: int("42") devuelve 42.

float()
# Descripción: Convierte un valor en un número de punto flotante (decimal).
# Ejemplo: float("3.14") devuelve 3.14.

type()
# Descripción: Devuelve el tipo de un objeto.
# Ejemplo: type(5) devuelve <class 'int'>.

max()
# Descripción: Devuelve el valor más grande de un iterable o de varios argumentos.
# Ejemplo: max(3, 5, 7) devuelve 7.

min()
# Descripción: Devuelve el valor más pequeño de un iterable o de varios argumentos.
# Ejemplo: min(3, 5, 7) devuelve 3.

sum()
# Descripción: Suma todos los elementos de un iterable (como una lista o tupla).
# Ejemplo: sum([1, 2, 3]) devuelve 6.

sorted()
# Descripción: Devuelve una lista con los elementos de un iterable ordenados.
# Ejemplo: sorted([3, 1, 2]) devuelve [1, 2, 3].

abs()
# Descripción: Devuelve el valor absoluto de un número.
# Ejemplo: abs(-5) devuelve 5.

round()
# Descripción: Redondea un número al número de decimales especificado.
# Ejemplo: round(3.14159, 2) devuelve 3.14.

input()
# Descripción: Permite al usuario ingresar datos desde el teclado. Devuelve la entrada como una cadena.
# Ejemplo: input("Introduce tu nombre: ") permite al usuario escribir un texto.

print()
# Descripción: Muestra información en la consola.
# Ejemplo: print("Hola, mundo!") imprime Hola, mundo!.

isinstance()
# Descripción: Verifica si un objeto es una instancia de una clase o de una subclase.
# Ejemplo: isinstance(5, int) devuelve True.

list()
# Descripción: Convierte un iterable en una lista.
# Ejemplo: list("Hola") devuelve ['H', 'o', 'l', 'a'].

tuple()
# Descripción: Convierte un iterable en una tupla.
# Ejemplo: tuple([1, 2, 3]) devuelve (1, 2, 3).

set()
# Descripción: Convierte un iterable en un conjunto (set), eliminando duplicados.
# Ejemplo: set([1, 2, 2, 3]) devuelve {1, 2, 3}.

dict()
# Descripción: Crea un diccionario vacío o a partir de una secuencia de pares clave-valor.
# Ejemplo: dict(a=1, b=2) devuelve {'a': 1, 'b': 2}.

zip()
# Descripción: Combina dos o más iterables en un solo iterable.
# Ejemplo: zip([1, 2, 3], ['a', 'b', 'c']) devuelve [(1, 'a'), (2, 'b'), (3, 'c')]

all()
# Descripción: Devuelve True si todos los elementos de un iterable son verdaderos (o si el iterable está vacío).
# Ejemplo: all([True, True, False]) devuelve False.

any()
# Descripción: Devuelve True si al menos un elemento de un iterable es verdadero.
# Ejemplo: any([False, False, True]) devuelve True.

zip()
# Descripción: Combina dos o más iterables elemento por elemento.
# Ejemplo: zip([1, 2, 3], ['a', 'b', 'c']) devuelve [(1, 'a'), (2, 'b'), (3, 'c')].

map()
# Descripción: Aplica una función a cada elemento de un iterable.
# Ejemplo: map(lambda x: x * 2, [1, 2, 3]) devuelve [2, 4, 6].

filter()
# Descripción: Filtra los elementos de un iterable, dejando solo aquellos que cumplen una condición.
# Ejemplo: filter(lambda x: x > 2, [1, 2, 3]) devuelve [3].

reduce()  # (requiere importar functools)
# Descripción: Aplica una función de forma acumulativa a los elementos de un iterable para reducirlo a un solo valor.
# Ejemplo: from functools import reduce; reduce(lambda x, y: x + y, [1, 2, 3]) devuelve 6.

enumerate()
# Descripción: Devuelve un objeto enumerado que contiene pares (índice, valor) de un iterable.
# Ejemplo: enumerate(['a', 'b', 'c']) devuelve [(0, 'a'), (1, 'b'), (2, 'c')].

join()
# Descripción: Une los elementos de un iterable (como una lista) en una única cadena, usando el string de la izquierda como separador.
# Ejemplo: " ".join(['Hola', 'mundo']) devuelve "Hola mundo".
Ejemplo: " ".join(['Hola', 'mundo'])  # devuelve "Hola mundo".

startswith()
# Descripción: Devuelve True si una cadena comienza con una subcadena específica.
# Ejemplo: "Hola mundo".startswith("Hola") devuelve True.

split()
# Descripción: Divide una cadena en una lista de subcadenas basadas en un delimitador.
# Ejemplo: "Hola mundo".split() devuelve ['Hola', 'mundo'].

replace()
# Descripción: Reemplaza una subcadena por otra en una cadena.
# Ejemplo: "Hola mundo".replace("mundo", "Python") devuelve "Hola Python".

find()
# Descripción: Devuelve el índice de la primera aparición de una subcadena en una cadena, o -1 si no se encuentra.
# Ejemplo: "Hola mundo".find("mundo") devuelve 5.

count()
# Descripción: Devuelve el número de veces que una subcadena aparece en una cadena.
# Ejemplo: "Hola mundo".count("o") devuelve 2.

upper()
# Descripción: Convierte todos los caracteres de una cadena a mayúsculas.
# Ejemplo: "hola".upper() devuelve "HOLA".

lower()
# Descripción: Convierte todos los caracteres de una cadena a minúsculas.
# Ejemplo: "HOLA".lower() devuelve "hola".

capitalize()
# Descripción: Convierte la primera letra de una cadena a mayúscula y el resto a minúsculas.
# Ejemplo: "hola".capitalize() devuelve "Hola".

strip()
# Descripción: Elimina los espacios en blanco al principio y al final de una cadena.
# Ejemplo: " Hola ".strip() devuelve "Hola".

all()
# Descripción: Devuelve True si todos los elementos del iterable son verdaderos o si el iterable está vacío.
# Ejemplo: all([True, True, False]) devuelve False

index()
# Descripcion: Sirve para ubicar la posición de un elemento en una lista o cadena.
# Ejemplo: lista.index(20)

count()
# Descripción: Devuelve el número de veces que un elemento aparece en una lista
# Ejemplo: lista.count(20)

union()
# Descripcion: Devuelve un nuevo conjunto que contiene todos los elementos de los conjuntos involucrados , eliminando los duplicados
# Ejemplo: conjunto1.union(conjunto2)
# conjunto1 = {1, 2, 3}
# conjunto2 = {3, 4, 5}
# union = conjunto1.union(conjunto2)
# print(union)  -> Salida: {1, 2, 3, 4, 5}

intersection()
# Descripcion: Devuelve un nuevo conjunto que contiene solos los elementos que esten en ambos conjuntos
# Ejemplo: conjunto1.intersection(conjunto2)
# conjunto1 = {1, 2, 3}
# conjunto2 = {2, 3, 4}
# interseccion = conjunto1.intersection(conjunto2)
# print(interseccion)  -> Salida: {2, 3}

difference()
# Descripcion: Devuelve un nuevo conjunto con elementos que esten en el primer conjunto pero no en el segundo
# Ejemplo: conjunto1.difference(conjunto2)
# conjunto1 = {1, 2, 3}
# conjunto2 = {2, 3, 4}
# diferencia = conjunto1.difference(conjunto2)
# print(diferencia)  -> Salida: {1}

symmetric_difference()
# Descripcion: Devuelve un nuevo conjunto que contiene los elementos de ambos conjuntos que no esten en ambos conjuntos
# Ejemplo: conjunto1.symmetric_difference(conjunto2)
# conjunto1 = {1, 2, 3}
# conjunto2 = {2, 3, 4}
# diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
# print(diferencia_simetrica)  -> Salida: {1, 4}

issubset()
# Descripcion: Devuelve True si el conjunto1 es un subconjunto de conjunto2.
# Ejemplo: conjunto1.issubset(conjunto2)
# conjunto1 = {1, 2}
# conjunto2 = {1, 2, 3, 4}
# es_subconjunto = conjunto1.issubset(conjunto2)
# print(es_subconjunto)  -> Salida: True

issuperset()
# Descripcion: Devuelve true si en el conjunto1 esta los elementos de conjunto 2
# Ejemplo: conjunto1.issuperset(conjunto2)
# conjunto1 = {1, 2, 3, 4}
# conjunto2 = {2, 3}
# es_superconjunto = conjunto1.issuperset(conjunto2)
# print(es_superconjunto)  -> Salida: True

isdisjoint()
# Descripcion: Devuelve true si los dos conjuntos tienen elementos totalmente distintos
# Ejemplo: conjunto1.isdisjoint(conjunto2)
# conjunto1 = {1, 2, 3}
# conjunto2 = {4, 5, 6}
# son_disjuntos = conjunto1.isdisjoint(conjunto2)
# print(son_disjuntos)  -> Salida: True
