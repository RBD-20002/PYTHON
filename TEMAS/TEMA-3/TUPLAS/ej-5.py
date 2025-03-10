"""
Escribir una función que reciba una tupla de números y un valor n y 
devuelva una lista con los elementos de la tupla que son múltiplos de n.
"""
def multiplosTupla(tupla:tuple =None , n:int =None):
    try:
        if not tupla or not n:
            raise TypeError("Falta un argumento")
        if not isinstance(tupla,tuple) or not isinstance(n,int):
            raise ValueError("La tupla y el valor deben ser de tipos correctos")
        return [num for num in tupla if num % n == 0]
    
    except TypeError as t:
        print(f"ERROR: {t}")
        return None
    except ValueError as v:
        print(f"ERROR: {v}")
        return None
    except:
        print("ERROR: fallo inesperado")
        return None
    
#Prueba
print(multiplosTupla((1,2,3,4,5,6),2))
print("-------------------------------")
print(multiplosTupla([1,2,3,4,5,6],3))
print("-------------------------------")
print(multiplosTupla([1,2,3,4,5,6]))
print("-------------------------------") 
print(multiplosTupla(3,(1,2,3,4,5,6)))
print("-------------------------------")
"""print(multiplosTupla(1,2,3,4,5))"""