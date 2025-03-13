"""
Escribir una función que reciba una lista de palabras y devuelva 
un conjunto con las palabras que tienen más de n caracteres.
"""
def palabras_mayor(lista:list , contador:int):
    try:
        return {palabra for palabra in lista if len(palabra) > contador}
    except TypeError:
        print("ERROR: La funcion necesita una lista y un entero en ese orden")
        return None
    
print(palabras_mayor(["hola", "como", "estas", "bien"], 4)) 
print("-"*20)
print(palabras_mayor(["hola", "como", "estas", "bien"], "b"))
print("-"*20)
print(palabras_mayor([],2))
print("-"*20)
print(palabras_mayor(1223,22))