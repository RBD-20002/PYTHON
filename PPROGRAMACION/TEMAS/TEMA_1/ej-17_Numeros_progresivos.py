"""Diseñar un algoritmo que lea números enteros positivos de teclado y sólo acepte como válidos aquellos que 
sean mayores que el anterior número leído. El algoritmo terminará cuando se introduzca el 0."""

contador = 0
num = int(input("Ingresa un numero inicial: "))
while True:
    numero = int(input("Ingrese un número entero positivo: "))
    if numero == 0:
        print("adios")
        break
    if numero > num:
        num = numero
    else:
        print("El número no es mayor que el anterior. Por favor, ingrese un número válido")
