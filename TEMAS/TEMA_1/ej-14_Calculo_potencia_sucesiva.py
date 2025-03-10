"""Diseñar un algoritmo que calcule la potencia para dos números naturales x e y mediante una 
acumulación sucesiva de productos. Previo al cálculo se verificará que ambos valores son positivos."""

base = int(input("Ingrese la base (x): "))
exponente = int(input("Ingrese el exponente (y): "))
if base > 0 and exponente > 0:
    resultado = 1
    for i in range(exponente):
        resultado *= base

print(f"La potencia de {base} elevado a {exponente} es : {resultado}")