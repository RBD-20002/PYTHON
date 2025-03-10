"""
Escribir una función que reciba una lista de enteros y devuelva otra lista sin elementos repetidos,
para ello se puede convertir la lista en un conjunto y después volver a convertirlo en lista.
"""

def eliminar_repetidos(lista:list):
    try:
        return list(set(lista))
    
    except TypeError:
        print("La funcion necesita una lista para poder ejecutarse")
    except:
        print("ERROR: fallo inesperado")
        
print(eliminar_repetidos([1,2,4,1,2,3,4,5,8,9]))
print("-"*20)
print(eliminar_repetidos([]))
print("-"*20)
print(eliminar_repetidos(123))