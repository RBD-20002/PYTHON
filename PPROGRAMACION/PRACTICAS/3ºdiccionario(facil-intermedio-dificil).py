print("<"+"-"*20+"Diccionarios|Nivel Facil|"+"-"*20+">")


"""1. Crea un diccionario que almacene el nombre de 5 países como claves y sus capitales como valores."""
#Ejemplo de Entrada:
Países = ['España', 'Francia', 'Italia', 'Portugal', 'Alemania']
Capitales = ['Madrid', 'París', 'Roma', 'Lisboa', 'Berlín']
#Ejemplo de Salida:
#{'España': 'Madrid', 'Francia': 'París', 'Italia': 'Roma', 'Portugal': 'Lisboa', 'Alemania': 'Berlín'}


def dict_pais(diccionario:list , diccionario2:list):
    diccionario = {}
    for i in range(len(Países)):
        diccionario[Países[i]] = Capitales[i]
    return diccionario

print(dict_pais(Países , Capitales))
    

print("-"*50)
"""2. Escribe un programa que recorra un diccionario e imprima las claves y valores en un formato legible."""
Entrada = {'España': 'Madrid', 'Francia': 'París'}
#Ejemplo de Salida:
#España -> Madrid
#Francia -> París


def recorrer_diccionario(diccionario:dict):
    for clave , valor in diccionario.items():
        print(f"{clave} -> {valor}" )

print(recorrer_diccionario(Entrada))


print("-"*50)
"""3. Agrega un nuevo par clave-valor a un diccionario existente."""
Entrada = {'España': 'Madrid'}
#Nuevo par: {'Francia': 'París'}
#Ejemplo de Salida: {'España': 'Madrid', 'Francia': 'París'}


def agregar_palabra(diccionario:dict):
    clave = input("Introduce la clave: ").capitalize()
    valor = input("Introduce el valor: ").capitalize()
    diccionario[clave] = valor
    return diccionario

print(agregar_palabra(Entrada))


print("-"*50)
"""4. Comprueba si una clave dada está en un diccionario y devuelve un mensaje apropiado."""
Entrada = {'España': 'Madrid'}
#Clave buscada: 'España'
#Ejemplo de Salida:
#La clave 'España' está en el diccionario.


def buscar_clave(diccionario:dict , palabra):
    for clave , valor in diccionario.items():
        if palabra == clave:
            return f"La clave '{palabra}' está en el diccionario."
        return f"La clave '{palabra}' no está en el diccionario."
    
print(buscar_clave(Entrada , "España"))
print(buscar_clave(Entrada , "Francia"))


print("-"*50)
print("<"+"-"*20+"Diccionarios|Nivel Intermedio|"+"-"*20+">")


"""1. Crea un diccionario que almacene productos como claves y sus precios como valores. 
Escribe una función para calcular el precio total de una lista de productos dada."""
#Ejemplo de Entrada:
Productos = {'manzana': 2, 'pan': 1.5, 'leche': 1.2}
Lista = ['manzana', 'pan']
Lista2 = ['manzana', 'pan', 'platano']
#Ejemplo de Salida:
#Total: 3.5


def compra_super(diccionario:dict , lista:list):
    total = 0
    for producto in lista:
        if producto in diccionario:
            total += diccionario[producto]
        return "Un articulo de la lista no se encuentra en los productos"
    return total

print(compra_super(Productos , Lista))
print(compra_super(Productos , Lista2))


print("-"*50)
"""2. Escribe un programa que invierta las claves y valores de un diccionario."""
Entrada = {'a': 1, 'b': 2}
#Ejemplo de Salida: {1: 'a', 2: 'b'}


def invertir_diccionario(diccionario:dict):
    salida = {}
    for clave , valor in diccionario.items():
        salida[valor] = clave 
    return salida

print(invertir_diccionario(Entrada))


print("-"*50)
"""3. Implementa un programa que elimine un par clave-valor si la clave cumple con una condición específica."""
Entrada = {'a': 1, 'b': 2, 'c': 3}
#Condición: clave empieza con 'b'
#Ejemplo de Salida: {'a': 1, 'c': 3}


def eliminar_clave(diccionario:dict , condicion:str):
    for clave , valor in list(diccionario.items()):
        if clave.startswith(condicion):
            del diccionario[clave]
    return diccionario

print(eliminar_clave(Entrada , "b"))


print("-"*50)
"""4. Convierte dos listas (una de claves y otra de valores) en un diccionario."""
#Ejemplo de Entrada:
Claves = ['a', 'b']
Valores = [10, 20]
#Ejemplo de Salida: {'a': 10, 'b': 20}


def convertir_diccionario(claves:list , valores:list):
    salida = {}
    for i in range(len(claves)):
        salida[claves[i]] = valores[i]
    return salida

print(convertir_diccionario(Claves , Valores))


print("-"*50)
print("<"+"-"*20+"Diccionarios|Nivel Dificil|"+"-"*20+">")


"""1. Escribe una función que combine dos diccionarios. Si hay claves repetidas, suma los valores."""
#Ejemplo de Entrada:
Dic1 = {'a': 1, 'b': 2}
Dic2 = {'b': 3, 'c': 4}
#Ejemplo de Salida: {'a': 1, 'b': 5, 'c': 4}


def sumar_diccionarios(diccionario1:dict , diccionario2:dict):
    salida = diccionario1.copy()
    for clave , valor in diccionario2.items():
        if clave in salida:
            salida[clave] += valor
        else:
            salida[clave] = valor
    return salida

print(sumar_diccionarios(Dic1 , Dic2))


print("-"*50)
"""2. Crea un diccionario anidado para representar un grupo de estudiantes y sus notas. 
Escribe una función para calcular el promedio de notas de un estudiante dado."""
#Ejemplo de Entrada:
estudiantes = {'Juan': [5, 6], 'Ana': [7, 8]}
#Estudiante: 'Ana'
#Ejemplo de Salida:
#Promedio: 7.5


def media_notas(diccionario:dict , estudiante:str):
    for alumnos , notas in diccionario.items():
        for nota in notas:
            if alumnos == estudiante:
                return f"El promedio de {estudiante} es {sum(notas) / len(notas)}"

print(media_notas(estudiantes , "Ana"))


print("-"*50)
"""3. Dado un diccionario de palabras y su frecuencia, encuentra la palabra más frecuente."""
Entrada = {'hola': 3, 'mundo': 5, 'python': 2}
#Ejemplo de Salida: 'mundo'


def palabra_más_frecuente(diccionario:dict):
    return max(diccionario , key = diccionario.get)

print(palabra_más_frecuente(Entrada))


print("-"*50)
"""4. Implementa un programa que ordene un diccionario por sus valores en orden descendente."""
Entrada = {'a': 3, 'b': 1, 'c': 2}
#Ejemplo de Salida: {'a': 3, 'c': 2, 'b': 1}


def ordenar_diccionario(diccionario:dict):
    for clave , valor in sorted(diccionario.items() , key = lambda item: item[1]):
        print(f"{clave}: {valor}" , end = " ")

print(ordenar_diccionario(Entrada))