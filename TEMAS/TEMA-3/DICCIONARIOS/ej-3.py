"""
Escribir una función que reciba un diccionario con los precios de distintos productos y 
un diccionario con los productos y la cantidad de cada uno que ha comprado un cliente y 
devuelva el precio total de la compra.
"""
def mercado(lista_compra):
    articulos = {"manzana": 2 , "platano": 1 , "pera": 3}
    total = 0
    for producto, cantidad in lista_compra.items():
        if producto in articulos:
            total += articulos[producto] * lista_compra[producto]
    return total    

# Pruebas
print(mercado({"manzana": 2, "platano": 1, "pera": 3}))  # Devuelve 11
print(mercado({"manzana": 1, "pera": 2}))  # Devuelve 5
print(mercado({"platano": 3, "pera": 1}))  # Devuelve 3
print(mercado({"manzana": 0, "pera": 1}))  # Devuelve 0
print(mercado({"manzana": 1, "platano": 1, "pera": 1}))  # Devuelve 4
