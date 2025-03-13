"""
Escribir una función que reciba una tupla de elementos e indique si es capicúa o no.
"""
def capicuaTupla(tupla:tuple =None):
    try:
        if not isinstance(tupla,tuple):
            raise TypeError("La funcion solo aceta tuplas")  
        return tupla == tupla[::-1]
    except TypeError as t:
        print(f"ERROR: {t}")
        return None

# Pruebas
print(capicuaTupla((1,2,3,3,2,1)))
print("---------------------------")
print(capicuaTupla((1,2,3,4,5,6)))
print("---------------------------")
print(capicuaTupla(()))
print("---------------------------")
print(capicuaTupla([1,2,3,4,5,6]))