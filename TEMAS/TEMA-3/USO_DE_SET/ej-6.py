"""
Escribir una función que dadas dos palabras devuelva un conjunto con las letras que tienen en común.
"""
def iguales_letras(palabra1:str , palabra2:str):
    try:
        return set(palabra1).intersection(palabra2)
    except TypeError:
        print("ERROR: Los argumentos introducidos deben ser iterables")
    except:
        print("ERROR: fallo inesperado")
    
print(iguales_letras("hola","como"))
print("-"*20)
print(iguales_letras("hola","hola"))
print("-"*20)
print(iguales_letras(4543,2324))
print("-"*20)
print(iguales_letras("hola", 2451))
print("-"*20)
print(iguales_letras("53532","2345432"))