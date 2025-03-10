"""Diseñar un algoritmo que lea del teclado tres números enteros y escriba en pantalla 
un mensaje indicando si al menos dos de esos tres números son pares."""

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
if (num1 % 2 == 0 and num3 % 2 == 0 and num2 % 2 == 0):
    print("Los tres números son pares.")
elif (num1 % 2 == 0 and num2 % 2 == 0) or (num2 % 2 == 0 and num3 % 2 == 0) or (num1 % 2 == 0 and num3 % 2 == 0):
    print("Al menos dos de los números son pares.")
else:
    print("Los tres numeros son impares.")