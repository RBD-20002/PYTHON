"""Diseñar un algoritmo que convierta una temperatura leída en grados 
Farenheit a grados Celsius, usando la fórmula: C=(5/9)*(F-32)"""

farenheit = int(input("Introduce valor de farenheit: "))
celsius = (5/9)*(farenheit-32)
print(f"La temperatura en grados celcius es: {celsius} ºC")