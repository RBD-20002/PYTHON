"""
Escribir una función que reciba una tupla de elementos e indique si 
se encuentran ordenados de menor a mayor o no.
"""
def mayorTupla(tupla:tuple =None):
    try:
        if tupla is None:
            raise TypeError("Falta el argumento de la tupla")
        if not isinstance(tupla,tuple):
            raise TypeError("La funcion solo acepta tuplas")
        for i in range(len(tupla)-1):
            if tupla[i] > tupla[i+1]:
                return False
            return True
    
    except TypeError as t:
        print(f"ERROR: {t}")
        return None        
    except:
        print("ERROR: fallo inesperado")
        return None

# Pruebas
print(mayorTupla((1, 2, 3, 4, 5))) 
print("--------------------------------")
print(mayorTupla((5, 4, 3, 2, 1)))  
print("--------------------------------")
print(mayorTupla([1,2,3,4,5,6]))  
print("--------------------------------")
print(mayorTupla(()))  
print("--------------------------------")
print(mayorTupla())