"""
Escribir una función que reciba una lista de números y devuelva su media. 
Si la lista está vacía debe devolver un mensaje de error.
"""
def media(lista:list = None):
    try:
        if not all(isinstance(x,int) for x in lista):
            raise TypeError("La lista solo puede contener numeros enteros")
        if not isinstance(lista,list):
            raise TypeError("El argumento solo puede ser una lista")
        return (sum(lista)/len(lista))
    
    except TypeError as t:
        print(f"ERROR:{t}")
        return None
    except ZeroDivisionError:
        print("ERROR: la lista no puede estar vacia")
        return None
    
# Pruebas
print(media([1,2,3,4,5]))
print("-------------------------------")
print(media((1,2,3,4,5)))
print("-------------------------------")
print(media([]))
print("-------------------------------")
print(media([1,"a",2,"b",3,"c"]))