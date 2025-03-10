"""
Escribir una función que reciba dos conjuntos y devuelva un conjunto con 
los elementos que están en ambos conjuntos.
"""

def juntar(conjunto1: set = None, conjunto2: set = None):
    try:
        return conjunto1.intersection(conjunto2)

    except AttributeError:
        print("ERROR: la funcion solo acepta conjuntos")
        return {}
    except Exception:
        print("ERROR: fallo inesperado")
        return {}


print(juntar({1, 2, 3, 4, 5}, {4, 5, 6, 7, 8, 9}))
print("-"*40)
print(juntar({1, 2, 3}, {6, 7, 8, 9}))
print("-"*40)
print(juntar({"a", 1, "a", 2, "b"}, {"a", 3, 2, "b"}))
print("-"*40)
print(juntar({(1, 2), (3, 4), (5, 6)}))
print("-"*40)
print(juntar(1234532))
