"""Diseñar un algoritmo que lea un conjunto de números reales, los cuente y calcule y muestre
la media, varianza y la desviación típica del conjunto de números. """
#Media = (suma de los números) / (número de números).
#Varianza = ((suma de los cuadrados de los números) - (suma de los números)^2 / (número de números)).
#La desviación típica es la raíz cuadrada de la varianza.

nº_pedidos = int(input("Cuantos numeros se van a pedir: "))
contador = 0
suma = 0
suma_cuadrados = 0
while contador < nº_pedidos:
    numero = float(input(f"Ingrese el numero {contador+1}: "))
    contador += 1
    suma += numero
    suma_cuadrados += numero**2
    media = suma / nº_pedidos
    varianza = (suma_cuadrados - (suma**2 / nº_pedidos))
    desviacion_tipica = varianza ** 0.5

print(media , varianza, desviacion_tipica)  