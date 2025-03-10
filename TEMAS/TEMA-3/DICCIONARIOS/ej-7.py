"""
Escribir una función que reciba una lista de palabras y devuelva un diccionario con 
las palabras como claves y el número de veces que aparecen como valor.
"""


def diccionarioContador(lista: list):
    diccionario = {}
    for palabras in lista:
        diccionario[palabras] = 0
    for palabras in lista:
        diccionario[palabras] += 1
    return diccionario

def diccionarioContador(list: list):
    return {palabra: lista.count(palabra) for palabra in lista}


lista = ["hola", "nombre", "hola", "nombre", "hola", "nombre", "juan"]

print(diccionarioContador(lista))
