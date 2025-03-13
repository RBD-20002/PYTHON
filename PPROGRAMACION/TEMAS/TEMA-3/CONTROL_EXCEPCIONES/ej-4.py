"""
Escribir una función que reciba una lista de números y devuelva una lista con los cuadrados de los números. 
Si la lista contiene algún elemento que no es un número debe devolver un mensaje de error.
"""
def cuadrados(lista:list =None):
    try:
        if not lista:
            raise ValueError("La lista no puede estar vacia")
        if not isinstance(lista,list):
            raise TypeError("La funcion solo acepta lista , no acepta tuplas , conjuntos ni diccionarios")
        if not all(isinstance(x,int) for x in lista):
            raise ValueError("La lista solo acepta numeros enteros")
        return [i ** 2 for i in lista]
    
    except TypeError as e:
        print(f"ERROR: {e}")
        return None
    except ValueError as e:
        print(f"ERROR: {e}")
        return None
    except Exception:
        print("ERROR: fallo inesperado")

# Pruebas
print(cuadrados([1, 2, 3, 4, 5]))  
print("-------------------------------")
print(cuadrados([1, 2, "3", 4, 5])) 
print("-------------------------------")
print(cuadrados((1,2,3,4,5)))
print("-------------------------------")
print(cuadrados(["a", "b", "c", "d","e"]))
print("-------------------------------")
print(cuadrados([ ]))