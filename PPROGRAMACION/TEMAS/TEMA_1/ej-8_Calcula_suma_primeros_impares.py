"""Realizar un algoritmo que calcule y muestre en la pantalla la suma de 
los n primeros enteros impares. El valor de n se solicitará al usuario."""

n = int(input("Introduce valor de n: "))
suma = 0
for i in range(1,(n*2)+1):
    if i % 2 != 0:
        suma += i

print("La suma de los primeros", n, "enteros impares es:", suma)