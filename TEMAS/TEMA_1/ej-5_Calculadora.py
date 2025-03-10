"""Diseñar un algoritmo que lea del teclado dos números enteros y un carácter. El caracter puede ser +, -, *, /, %, ^
y en función del carácter introducido se mostrará el resultado de la operación correspondiente. """

num1 = int(input("Introduce num1: "))
num2 = int(input("Introduce num2: "))
operador = input("Introduce un operador (+ , - , * , / , % , ** , //): ")
if operador == "+":
    print(num1 + num2)

elif operador == "-":
    print(num1 - num2)

elif operador == "*":
    print(num1 * num2)

elif operador == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error: No se puede dividir por cero.")

elif operador == "%":
    if num2 != 0:
        print(num1 % num2)
    else:
        print("Error: No se puede dividir por cero.")

elif operador == "**":
    print(num1 ** num2)

elif operador == "//":
    if num2 != 0:
        print(num1 // num2)
    else:
        print("Error: No se puede dividir por cero.")
