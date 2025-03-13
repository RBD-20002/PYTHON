"""
Escribir una función que reciba una tupla de elementos e indique si son todos distintos o no.
"""
def diferenteElementos(tupla:tuple =None):
    try:
        if not isinstance(tupla,tuple):
            raise TypeError("La funcion solo acepta tuplas")
        for i in range(len(tupla)):
            for j in range(i+1 , len(tupla)):
                if tupla [i] == tupla[j]:
                    return False
            return True

    except TypeError as t:
        print(f"ERROR: {t}")
        return None
    except Exception:
        print("ERROR: fallo inesperado")
        return None
    
# Pruebas 
print(diferenteElementos((1, 2, 3, 4, 5))) 
print("-------------------------------")
print(diferenteElementos((1, 1, 1, 1, 1)))  
print("-------------------------------")
print(diferenteElementos((1,)))
print("-------------------------------")
print(diferenteElementos([1,2,3,4,5,9]))
print("-------------------------------")
print(diferenteElementos((1,"b",2,"c",3,"d",4)))