# Enunciado completo: Gestión de una concesionaria de coches
# Escribe un programa en Python para gestionar los datos de una concesionaria de coches. El sistema debe permitir almacenar, organizar y consultar información de los vehículos disponibles en la concesionaria utilizando diccionarios, listas, tuplas y/o conjuntos.

# Requisitos funcionales:
# Estructura de los datos:

# Cada coche debe representarse mediante un diccionario con los siguientes campos:
# marca (cadena): Marca del coche (e.g., "Toyota").
# modelo (cadena): Modelo del coche (e.g., "Corolla").
# año (entero): Año de fabricación (e.g., 2020).
# matricula (cadena): Matrícula del coche (e.g., "ABC123").
# estado (cadena): Indica si el coche es "nuevo" o "usado".
# color (cadena): Color del coche (e.g., "Rojo").
# precio (flotante): Precio del coche (e.g., 15000.50).
# Todos los coches deben almacenarse en una lista.
# Funciones requeridas:

# Agregar un coche: Solicitar al usuario los datos de un coche y añadirlo a la lista.
# Listar coches: Mostrar todos los coches almacenados, ordenados por año de fabricación.
# Filtrar coches:
# Por marca.
# Por estado (nuevo o usado).
# Eliminar un coche: Permitir eliminar un coche por su matrícula.
# Estadísticas básicas:
# Cantidad total de coches.
# Precio promedio de los coches.
# Datos de entrada y salida esperados
# Ejemplo 1: Agregar coches
# Entrada del usuario:

# makefile
# Copiar código
# Agregar un coche:
# Marca: Toyota
# Modelo: Corolla
# Año: 2020
# Matrícula: ABC123
# Estado (nuevo/usado): usado
# Color: Blanco
# Precio: 15000.50
# Salida esperada:

# Copiar código
# Coche agregado con éxito.
# Ejemplo 2: Listar coches
# Entrada del usuario:

# Copiar código
# Listar coches
# Salida esperada (ordenados por año):

# yaml
# Copiar código
# Listado de coches disponibles:
# 1. Marca: Honda | Modelo: Civic | Año: 2018 | Matrícula: XYZ789 | Estado: usado | Color: Gris | Precio: 12000.00
# 2. Marca: Toyota | Modelo: Corolla | Año: 2020 | Matrícula: ABC123 | Estado: usado | Color: Blanco | Precio: 15000.50
# Ejemplo 3: Filtrar coches por marca
# Entrada del usuario:

# yaml
# Copiar código
# Filtrar por marca:
# Marca: Toyota
# Salida esperada:

# yaml
# Copiar código
# Coches de la marca Toyota:
# 1. Marca: Toyota | Modelo: Corolla | Año: 2020 | Matrícula: ABC123 | Estado: usado | Color: Blanco | Precio: 15000.50
# Ejemplo 4: Eliminar un coche
# Entrada del usuario:

# makefile
# Copiar código
# Eliminar coche
# Matrícula: ABC123
# Salida esperada:

# Copiar código
# Coche con matrícula ABC123 eliminado con éxito.
# Ejemplo 5: Estadísticas básicas
# Entrada del usuario:

# Copiar código
# Ver estadísticas
# Salida esperada:

# yaml
# Copiar código
# Estadísticas de la concesionaria:
# - Total de coches: 3
# - Precio promedio: 14000.33
# Instrucciones adicionales:
# Usa funciones para cada operación (agregar, listar, filtrar, eliminar, estadísticas).
# Organiza los datos de forma eficiente utilizando listas, diccionarios, tuplas y/o conjuntos según el caso.
# Asegúrate de manejar entradas incorrectas, como años no válidos o precios negativos.