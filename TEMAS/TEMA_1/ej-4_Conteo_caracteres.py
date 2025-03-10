"""Diseñar un algoritmo que lea 20 caracteres de teclado y muestre por 
pantalla el número de veces que se repiten cada una de las vocales."""

a = 0
e = 0
i = 0
o = 0
u = 0

print("Ingrese 20 caracteres (si ingresa más de 20 no se tendrán en cuenta)")
caracteres = input().lower()
if len(caracteres) > 20:
    vueltas = 20
else:
    vueltas = len(caracteres)

for x in range(vueltas):
    match caracteres[x]:
        case "a":
            a += 1
        case "e":
            e += 1
        case "i":
            i += 1
        case "o":
            o += 1
        case "u":
            u += 1

print("Cantidad de vocales a: " + str(a))
print("Cantidad de vocales e: " + str(e))
print("Cantidad de vocales i: " + str(i))
print("Cantidad de vocales o: " + str(o))
print("Cantidad de vocales u: " + str(u))