"""Diseñar un algoritmo que calcule y muestre en pantalla el factorial de un número entero dado."""


numero = int(input("Ingrese un número entero: "))
factorial = 1
if numero < 0:
    print("No se puede calcular el factorial de un número negativo.")
else:
    for i in range(1 , numero+1):
        factorial *= i
    print("El factorial de", numero, "es", factorial)