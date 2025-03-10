print("<"+"-"*30+"DICCIONARIO"+"-"*30+">")

# Escribir un programa que cree un diccionario con claves de cadena y
# valores de enteros y luego imprima el valor asociado a una clave dada.

def crear_diccionario():
    try:
        diccionario = {}
        nº_valores = int(input("Introduce cuantos valores habra en el diccionario: "))
        for i in range(nº_valores):
            clave = input(f"Introduce la clave {i+1}: ")
            valor = int(input(f"Introduce el valor de {clave}: "))
            diccionario[clave] = valor
        for clave, valor in diccionario.items():
            print(f"La clave {clave} tiene el valor {valor}")
        return diccionario
    except ValueError:
        print("ERROR: Debes introducir un valor numerico")
    except:
        print("ERROR: fallo inesperado")

"""print(crear_diccionario())"""

# Escribir un programa que reciba una lista de tuplas y cree un diccionario
# a partir de ella, donde cada tupla contiene una clave y un valor.

def a(lista):
    diccionario1 = {}
    for tuplas in lista:
        for j in tuplas:
            clave = [j]
            valor = input(f"Introduce el valor de {clave}: ")
            diccionario1[j] = valor
            print(f"{clave} tiene el valor {valor}")
    return print(diccionario1)

"""a([(1, 2), (3, 4), (5, 6)])"""

# Escribir un programa que itere sobre las claves y valores de un diccionario y realizar alguna operación con ellos.

# Escribir un programa que elimine las claves duplicadas de un diccionario y devuelva un nuevo diccionario con las claves únicas.

def eliminar_claves_duplicadas(diccionario):
    diccionario = dict(diccionario)
    diccionario_sin_duplicados = {}
    for clave in diccionario:
        if clave not in diccionario_sin_duplicados:
            diccionario_sin_duplicados[clave] = diccionario[clave]
    return diccionario_sin_duplicados
    
"""diccionario = {"a" : 1 , "b" : 2 , "c" : 3 , "a" : 1} 
print(eliminar_claves_duplicadas(diccionario))
lista_pares = [('a', 1), ('b', 2), ('a', 3), ('c', 4)]
print(eliminar_claves_duplicadas(lista_pares))"""

# Escribir un programa que determine si existe una clave específica en un diccionario dado.

def valor_en_diccionario(diccionario:dict , clave):
    for clav , valor in diccionario.items():
        if clave == clav:
            return True
    return False
    

"""diccionario = {"a" : 1 , "b" : 2 , "c" : 5}
print(valor_en_diccionario(diccionario , "a"))
print(valor_en_diccionario(diccionario, "d"))"""