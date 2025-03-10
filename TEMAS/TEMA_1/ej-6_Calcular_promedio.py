"""Diseñar un algoritmo que obtenga el promedio de una lista de varlores reales 
leídos por teclado. El algoritmo terminará cuándo el usuario introduzca 20 valores."""

nº_pedidos = int(input("Nº pedidos: "))
suma = 0
for i in range(nº_pedidos):
    valor = float(input(f"Valor {i+1}: "))
    suma += valor

print(f"La media es {suma} / {nº_pedidos}")