"""
Escribir una función que reciba una lista de números y devuelva el número más grande. 
Si la lista está vacía debe devolver un mensaje de error.
"""


def listaMayor(lista: list):
    try:
        if not lista:
            raise TypeError("La lista no puede estar vacia")
        if not isinstance(lista, list):
            raise TypeError("La función solo acepta lista, no acepta tuplas, conjuntos ni diccionarios")
        primer_tipo = type(lista[0])
        if not all(isinstance(x,primer_tipo)for x in lista):
            raise ValueError("La lista solo acepta valores del mismo tipo")
        return max(lista)
    
    except TypeError as t:
        print(f"ERROR: {t}")
        return None
    except ValueError as v:
        print(f"ERROR: {v}")
    except Exception:
        print("ERROR: fallo inesperado")

# Pruebas
print(listaMayor([5, 10, 3, 8, 2]))
print("-------------------------------")
print(listaMayor([]))
print("-------------------------------")
print(listaMayor([1, "a", 2, "b", 3, "c"]))
print("-------------------------------")
print(listaMayor((5, 10, 3, 8, 2)))
print("-------------------------------")
print(listaMayor(["a", "z", "b", "x", "p"]))
