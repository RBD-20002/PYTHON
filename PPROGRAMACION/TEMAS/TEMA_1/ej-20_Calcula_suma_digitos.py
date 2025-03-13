"""Diseñar un algoritmo que lea un número entero de teclado, visualice sus dígitos y calcule la suma de los dígitos que sean pares. 
Para extraer los dígitos de un número usaremos un bucle que divida el número por 10 sucesivamente. 
El resto de cada división corresponde a cada uno de los dígitos."""

numero = int(input("Introduce un numero: "))
suma = 0
for i in range(len(str(numero))):
    digito = numero % 10
    numero //= 10 
    suma += digito
print(suma)