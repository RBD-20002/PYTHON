"""Diseñar un algoritmo que calcule la suma de todos los números comprendidos 
entre 1 y 500 que cumplan la condición de ser múltiplos de 5 y de 7."""

suma = 0
for i in range(1,501):
    if i % 5 == 0 and i % 7 == 0:
        print(i)
        suma += i

print(suma)