"""
Escribir una función que reciba una tupla de números y devuelva 
la tupla con sus elementos ordenados de menor a mayor.
"""
def  ordenar(tupla:tuple =None):
    try:
        if not isinstance(tupla, tuple):
            raise TypeError("La funcion solo acepta tuplas")
        return sorted(tupla)
    
    except TypeError as t:
        print("ERROR: la funcion no acepta el argumento introducido")
        return None
    except Exception:
        print("ERROR: fallo inesperado")
        return None
    
# Pruebas
print(ordenar((25,48,96,4,74,)))
print("--------------------------------")
print(ordenar((1,"a",2,"b",3)))
print("--------------------------------")
print(ordenar(()))