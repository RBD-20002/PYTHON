"""Diseñar un algoritmo que lea una secuencia de 20 números reales introducidos por teclado. 
Al acabar la secuencia, debe mostrar el valor máximo y mínimo introdcidos."""

nº_pedidos = int(input("Cuantos numeros se van a pedir: "))
contador = 0
max = float('-inf') 
min = float('inf')
while contador < nº_pedidos:
    num = int(input(f"Introduce numero {contador+1}: "))
    if num > max:
        max = num
    if num < min:
        min = num
    contador += 1
    print(f"El maximo es {max} y el minimo es {min}")
    