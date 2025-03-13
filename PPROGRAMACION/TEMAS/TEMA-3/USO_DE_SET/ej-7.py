"""
Escribir una función que reciba dos listas y nos diga si la primera
lista está contenida en la segunda o no, utiliza operadores de conjuntos para ello.
"""


def lista_contenida(lista1: list, lista2: list):
    try:
        if not isinstance(lista1, list) or not isinstance(lista2, list):
            raise TypeError("Ambos argumentos deben ser listas")
        return set(lista1).issuperset(lista2)
    except TypeError as t:
        print(f"ERROR: {t}")
    except:
        print("ERROR: fallo inesperado")


print(lista_contenida([1, 2, 3, 4, 5, 6], [1, 2, 3]))
print("-"*20)
print(lista_contenida([1, 2, 3, 4, 5, 6], [7, 8, 9]))
print("-"*20)
print(lista_contenida([1, 2, 3, 4, 5], {}))
print("-"*20)
print(type(lista_contenida([1, 2, 3], 5)))
