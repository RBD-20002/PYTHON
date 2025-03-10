"""Diseñar un algoritmo que calcule y muestre en pantalla 
el volumen y el área de una esfera para un radio dado"""

import math
radio = float(input("Introduce el valor del radio: "))
area = 4 * math.pi * (radio ** 2)
volumen = (4/3) * math.pi * (radio ** 3)
print(f"El area de la esfera es {area} y el volumen es {volumen}")