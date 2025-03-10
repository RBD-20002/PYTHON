print("<"+"-"*30+"TUPLAS - DICCIONARIO"+"-"*30+">")

# Escribir un programa que cree una tupla con claves de cadena y valores de enteros y luego cree un diccionario a partir de ella.

def crear_tupla():
    nº_valores = int(input("Introduce el número de valores: "))
    tupla = []
    for i in range(nº_valores):
        clave = input("Introduce la clave: ").capitalize()        
        valor = int(input(f"Introduce el valor de {clave}: "))
        tupla.append((clave,valor))
        diccionario = dict(tupla)
    return dict(diccionario) 
   
"""print(crear_tupla())"""

# Escribir un programa que itere sobre una tupla de diccionarios y realizar alguna operación con ellos.

def calculo_diccionarios(diccionario:dict , clave1:str , clave2:str):
    y = None
    x = None
    for clave , valor in diccionario.items():    
        if clave== clave1:
            x = valor
        if clave == clave2:
            y = valor
    resultado = x + y
    print(resultado)
    
diccionario = {"a" : 10 , "b" : 50 , "c" : 5 , "d" : 15}

calculo_diccionarios(diccionario , "c" , "b")
