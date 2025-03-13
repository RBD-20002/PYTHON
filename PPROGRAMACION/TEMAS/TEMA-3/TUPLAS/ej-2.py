"""
Escribir una función que reciba una tupla de elementos e indique si 
se encuentran ordenados de mayor a menor o no.
"""
def menorTupla(tupla:tuple =None):
    try:
        if tupla is None:
            raise TypeError("Debe haber una tupla para la funcion")
        if not isinstance(tupla,tuple):
            raise TypeError("El argumento debe ser una tupla")
        if not all(isinstance(x,int) for x in tupla):
            raise TypeError("La tupla debe contener los mismos elementos")
        for i in range(len(tupla)-1):
            if tupla[i] < tupla[i+1]:
                return False
            
        return True
    
    except TypeError as t:
        print(f"ERROR: {t}")
        return None
    except Exception:
        print("ERROR: fallo inesperado")
        return None

# Ejemplos
print(menorTupla((5,4,3,2,1)))
print("-----------------------------")
print(menorTupla((5, 3, 1, 2, 4)))   
print("-----------------------------")
print(menorTupla([5, 3, 1, 2, 5]))     
print("-----------------------------")
print(menorTupla((5, 3, 1, 2, "a")))  
print("-----------------------------")
print(menorTupla())              
    