"""
Escribir una función que reciba una lista de palabras y devuelva un diccionario 
con las palabras como claves y su longitud como valor.
"""
def longitudPalabras(lista:list ): 
    diccionario = {}
    for palabra in lista:
        diccionario[palabra] = len(palabra)
    return diccionario
    
def longitudLista(lista:list):
    return {palabra: len(lista) for palabra in lista}

lista =["juan","ari","ded","barca","roberto","nexxuz"]
print(longitudPalabras(lista))