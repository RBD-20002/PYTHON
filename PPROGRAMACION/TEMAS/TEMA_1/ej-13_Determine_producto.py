"""Diseñar un algoritmo, que dados dos números, determine si su 
producto es positivo, nulo o negativo, sin realizar la multiplicación."""

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if (num1 > 0 and num2 > 0) or (num1 < 0 and num2 < 0):
    print("El producto sera positivo")
else:
    print("El producto sera negativo")