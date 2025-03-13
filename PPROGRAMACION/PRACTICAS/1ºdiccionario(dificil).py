print("<"+"-"*20+"Diccionarios|Nivel Difícil|"+"-"*20+">")

"""Ejercicio 1: Dado un diccionario de ventas mensuales por empleado, selecciona aleatoriamente un empleado y calcula el promedio de sus ventas"""
Entrada = {'Juan': [1200, 1500, 1300], 'María': [1700, 1600, 1800], 'Carlos': [1100, 1050, 1150]}
#Salida esperada: Ejemplo de salida esperada: 'Juan' -> Promedio: 1333.33

def promedio_empleado(diccionario:dict , empleado:str):
    for empleados , ventas in diccionario.items():
        if empleados == empleado:
            venta = round(sum(ventas) / len(ventas) , 2)
    return venta

print(promedio_empleado(Entrada , "Juan"))
            
"""Ejercicio 2: Usa un diccionario con estudiantes y sus calificaciones en varias materias. Selecciona un estudiante y calcula su calificación promedio."""
Entrada = {'Pedro': {'Matemáticas': 85, 'Ciencias': 90}, 'Ana': {'Historia': 88, 'Ciencias': 92}}
#Salida esperada: Ejemplo de salida esperada: 'Pedro' -> Promedio: 87.5

def promedio_estudiante(diccionario:dict , estudiante:str):
    for estudiantes , materias in diccionario.items():
        total_notas = 0
        if estudiantes == estudiante:
            for materia , notas in materias.items():
                    total_notas += notas
            promedio = total_notas / len(materias)
        
    return f"{estudiante} -> {promedio}"

print(promedio_estudiante(Entrada , "Pedro"))

"""Ejercicio 3: Crea un diccionario con productos y listas de precios históricos. Selecciona un producto y encuentra su precio más alto."""
Entrada = {'Café': [2.5, 2.8, 2.6], 'Pan': [1.0, 1.2, 1.1]}
#Salida esperada: Ejemplo de salida esperada: 'Café' -> Precio máximo: 2.8

def precio_maximo(diccionario:dict , producto:str):
    for productos , precios in diccionario.items():
        if productos == producto:
            precio_maximo = max(precios)
    return f"{producto} -> Precio maximo: {precio_maximo}"

print(precio_maximo(Entrada , "Pan"))

"""Ejercicio 4: Dado un diccionario de palabras y sus frecuencias en un texto, selecciona una palabra y muestra su frecuencia."""
Entrada = {'Python': 45, 'es': 30, 'genial': 15}
#Salida esperada: Ejemplo de salida esperada: 'genial' -> Frecuencia: 15

def frecuencia_palabra(diccionario:dict , palabra:str):
    for palabras , frecuencia in diccionario.items():
        if palabras == palabra:
            return f"{palabra} -> Frecuencia: {frecuencia}"
        
print(frecuencia_palabra(Entrada , "genial"))

"""Ejercicio 5: Crea un diccionario con países, sus ciudades principales y las poblaciones de estas ciudades. Selecciona un país y calcula la población total de sus ciudades."""
Entrada = {'España': {'Madrid': 3200000, 'Barcelona': 1600000}, 'Francia': {'París': 2200000, 'Lyon': 520000}}
#Salida esperada: Ejemplo de salida esperada: 'España' -> Población total: 4800000

def poblacion_total(diccionario:dict , pais:str):
    for paises , ciudades in diccionario.items():
        if paises == pais:
            poblacion = 0
            for ciudad , ciudadano in ciudades.items():
                poblacion += ciudadano
    return f"{pais} -> Población total: {poblacion}"

print(poblacion_total(Entrada , "Francia"))

"""Ejercicio 6: Usa un diccionario con películas, sus géneros y las calificaciones. Selecciona una película y muestra su género y calificación."""
Entrada = {'Inception': {'Género': 'Ciencia ficción', 'Calificación': 9.0}, 'Titanic': {'Género': 'Romance', 'Calificación': 8.5}}
#Salida esperada: Ejemplo de salida esperada: 'Titanic' -> Género: Romance, Calificación: 8.5

def mostrar_pelicula(diccionario:dict , pelicula:str):
    for peliculas , datos in diccionario.items():
        if peliculas == pelicula:
            return f"{pelicula} -> Género: {datos['Género']} , Calificación: {datos['Calificación']}"

print(mostrar_pelicula(Entrada , "Titanic"))
        
"""Ejercicio 7: Dado un diccionario con empleados y su historial de horas trabajadas por semana, selecciona un empleado y calcula sus horas totales trabajadas."""
Entrada = {'Laura': [40, 42, 38], 'José': [45, 48, 50]}
#Salida esperada: Ejemplo de salida esperada: 'José' -> Total: 143 horas

def total_horas(diccionario:dict , empleado:str):
    for empleados , horas in diccionario.items():
        if empleados == empleado:
            return f"{empleado} -> Total: {sum(horas)} horas"
        
print(total_horas(Entrada , "José"))

"""Ejercicio 8: Crea un diccionario con categorías de productos y listas de productos. Selecciona una categoría y muestra todos sus productos."""
Entrada = {'Frutas': ['Manzana', 'Banana'], 'Verduras': ['Zanahoria', 'Lechuga']}
#Salida esperada: Ejemplo de salida esperada: 'Verduras' -> ['Zanahoria', 'Lechuga']

def mostrar_categoria(diccionario:dict , categoria:str):
    for tipos, productos in diccionario.items():
        if tipos == categoria:
            return f"{categoria} -> {productos}"
        
print(mostrar_categoria(Entrada , "Verduras"))

"""Ejercicio 9: Usa un diccionario de meses con listas de temperaturas diarias. Selecciona un mes y calcula la temperatura promedio del mes."""
Entrada = {'Enero': [15, 16, 15, 14], 'Febrero': [13, 14, 15]}
#Salida esperada: Ejemplo de salida esperada: 'Enero' -> Promedio: 15.0°C

def promedio_temperatura(diccionario:dict , mes:str):
    for meses , temperaturas in diccionario.items():
        if meses == mes:
            return f"{mes} -> Promedio: {sum(temperaturas) / len(temperaturas)}°C"
        
print(promedio_temperatura(Entrada , "Enero"))

"""Ejercicio 10: Dado un diccionario con nombres de equipos y sus puntuaciones en diferentes partidos, selecciona un equipo y encuentra su puntuación máxima."""
Entrada = {'Equipo A': [3, 1, 4, 2], 'Equipo B': [5, 2, 3, 1]}
#Salida esperada: Ejemplo de salida esperada: 'Equipo A' -> Máximo: 4

def max_puntuacion(diccionario:dict , equipo:str):
    for equipos , puntuaciones in diccionario.items():
        if equipos == equipo:
            return f"{equipo} -> Maximo: {max(puntuaciones)}"
        
print(max_puntuacion(Entrada , "Equipo A"))