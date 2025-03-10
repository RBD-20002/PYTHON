print("<"+"-"*20+"Diccionarios|Nivel Intermedio|"+"-"*20+">")

"""Ejercicio 1: Dado un diccionario de estudiantes con sus calificaciones, selecciona un estudiante aleatorio y su calificación."""
Entrada = {'Juan': 85, 'María': 90, 'Carlos': 78, 'Ana': 92}
#Salida esperada: Ejemplo de salida esperada: 'Carlos' -> 78

def hallar_nota(diccionario:dict , nombre:str):
    for nombres , calificacion in diccionario.items():
        if nombres == nombre:
            return f"{nombre} -> {calificacion}"
        
print(hallar_nota(Entrada , "Juan"))

print("-"*50)
"""Ejercicio 2: Crea un diccionario con países y sus capitales. Selecciona un país y muestra su capital."""
Entrada = {'España': 'Madrid', 'Francia': 'París', 'Alemania': 'Berlín', 'Italia': 'Roma'}
#Salida esperada: Ejemplo de salida esperada: 'Francia' -> 'París'

def hallar_capital(diccionario:dict , pais:str):
    for paises , capitales in diccionario.items():
        if paises == pais:
            return f"{pais} -> {capitales}"
    
print(hallar_capital(Entrada , "Francia"))

print("-"*50)
"""Ejercicio 3: Usa un diccionario con colores y sus códigos hexadecimales. Selecciona un color y muestra su código."""
Entrada = {'Rojo': '#FF0000', 'Verde': '#00FF00', 'Azul': '#0000FF'}
#Salida esperada: Ejemplo de salida esperada: 'Azul' -> '#0000FF'

def hallar_codigo(diccionario:dict , color:str):
    for colores , codigos in diccionario.items():
        if colores == color:
            return f"{color} -> {codigos}"
        
print(hallar_codigo(Entrada , "Azul"))

print("-"*50)
"""Ejercicio 4: Dado un diccionario con productos y sus precios, selecciona un producto y muestra su precio."""
Entrada = {'Café': 2.5, 'Pan': 1.0, 'Leche': 1.2, 'Azúcar': 0.8}
#Salida esperada: Ejemplo de salida esperada: 'Pan' -> 1.0

def precio_producto(diccionario:dict , producto:str):
    for productos , precios in diccionario.items():
        if productos == producto:
            return f"{producto} -> {precios}"

print(precio_producto(Entrada , "Azúcar"))

print("-"*50)
"""Ejercicio 5: Crea un diccionario con nombres de personas y sus edades. Selecciona aleatoriamente una persona y muestra su edad."""
Entrada = {'José': 30, 'Laura': 25, 'Pedro': 28, 'Ana': 35}
#Salida esperada: Ejemplo de salida esperada: 'Pedro' -> 28

def hallar_edad(diccionario:dict , nombre:str):
    for nombres , edades in diccionario.items():
        if nombres == nombre:
            return f"{nombre} -> {edades} años"

print(hallar_edad(Entrada , "Pedro"))

print("-"*50)
"""Ejercicio 6: Dado un diccionario con números y sus cuadrados, selecciona un número y muestra su cuadrado."""
Entrada = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
#Salida esperada: Ejemplo de salida esperada: 3 -> 9

def hallar_potencia(diccionario:dict , numero:int):
    for numeros , potencias in diccionario.items():
        if numeros == numero:
            return f"{numero} -> {potencias}"

print(hallar_potencia(Entrada , 5))

print("-"*50)
"""Ejercicio 7: Crea un diccionario con estudiantes y sus asignaturas favoritas. Selecciona un estudiante y muestra su asignatura favorita."""
Entrada = {'Pedro': 'Matemáticas', 'Ana': 'Ciencias', 'Luis': 'Historia'}
#Salida esperada: Ejemplo de salida esperada: 'Luis' -> 'Historia'

def hallar_asignatura(diccionario:dict , estudiante:str):
    for estudiantes , asignaturas in diccionario.items():
        if estudiantes == estudiante:
            return f"{estudiante} -> {asignaturas}"

print(hallar_asignatura(Entrada , "Luis"))

print("-"*50)
"""Ejercicio 8: Usa un diccionario con meses y el número de días que tiene cada uno. Selecciona un mes y muestra el número de días."""
Entrada = {'Enero': 31, 'Febrero': 28, 'Marzo': 31, 'Abril': 30}
#Salida esperada: Ejemplo de salida esperada: 'Marzo' -> 31

def hallar_dias(diccionario:dict , mes:str):
    for meses , dias in diccionario.items():
        if meses == mes:
            return f"{mes} -> {dias} días"
        
print(hallar_dias(Entrada , "Marzo"))

print("-"*50)
"""Ejercicio 9: Dado un diccionario con palabras y sus definiciones, selecciona una palabra y muestra su definición."""
Entrada = {'Python': 'Lenguaje de programación', 'Diccionario': 'Colección de palabras y definiciones'}
#Salida esperada: Ejemplo de salida esperada: 'Python' -> 'Lenguaje de programación'

def hallar_definicion(diccionario:dict , palabra:str):
    for palabras , definiciones in diccionario.items():
        if palabras == palabra:
            return f"{palabra} -> {definiciones}"
        
print(hallar_definicion(Entrada , "Python"))

print("-"*50)
"""Ejercicio 10: Crea un diccionario con nombres de ciudades y sus países. Selecciona una ciudad y muestra su país."""
Entrada = {'Madrid': 'España', 'París': 'Francia', 'Roma': 'Italia'}
#Salida esperada: Ejemplo de salida esperada: 'Roma' -> 'Italia'

def hallar_pais(diccionario:dict , ciudad:str):
    for ciudades , paises in diccionario.items():
        if ciudades == ciudad:
            return f"{ciudad} -> {paises}"

print(hallar_pais(Entrada , "Roma"))