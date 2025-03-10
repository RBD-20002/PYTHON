"""
Escribir una función que reciba una tupla y una posición y devuelva el elemento de la tupla en la posición indicada. 
Si la posición es mayor que la longitud de la tupla debe devolver un mensaje de error.
"""
def posicionTupla(tupla:tuple , posicion:int):
    try:
        if not tupla:
            raise TypeError("La tupla esta vacia")
        if not isinstance(tupla,tuple):
            raise TypeError("La funcion solo acepta como primer argumento una tupla")
        if not isinstance(posicion,int):
            raise TypeError("El argumento posicion solo acepta tipos interos")
        return tupla[posicion]

    except TypeError as t:
        print(f"ERROR: {t}")
        return None
    except Exception:
        print("ERROR: fallo inesperado")
        return None
    

# Ejemplos:
print(posicionTupla((1,2,3,4,5,6),3))
print("-------------------------------")
print(posicionTupla([1,2,3,4,5,6],3))
print("-------------------------------")
print(posicionTupla((1,2,3,4,5,6),7))
print("-------------------------------")
print(posicionTupla((1,2,3,4,5,"55"),2))
print("-------------------------------")
print(posicionTupla((1,2,3,4,5,6),"5"))
print("-------------------------------")
print(posicionTupla((),5))