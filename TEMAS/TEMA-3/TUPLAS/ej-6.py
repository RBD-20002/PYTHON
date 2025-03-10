"""
Escribir una función que reciba una tupla de números y devuelva su máximo y su mínimo.
"""
def maximoMinimo(tupla:tuple =None):
    try:
        if not isinstance(tupla, tuple):
            raise TypeError("La funcion solo admite tuplas")
        if not all(isinstance(x,int,str) for x in tupla):
            raise TypeError("La tupla solo puede contener numeros enteros o strings")
        return [max(tupla) , min(tupla)]
    
    except TypeError as t:
        print(f"ERROR: {t}")
    except Exception:
        print("ERROR: fallo inesperado")

print(maximoMinimo((1,2,3,4,5)))
print("----------------------------")
print(maximoMinimo([1,2,3,4,5]))
print("----------------------------")
print(maximoMinimo(12234))
print("----------------------------")
print(maximoMinimo((1,"a",2,"b",3,"d")))