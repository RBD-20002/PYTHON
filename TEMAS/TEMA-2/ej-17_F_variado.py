def ingresar_lista():
    lista = []
    nº_pedidos = int(input("¿Cuantos valores quieres ingresar?: "))
    for i in range(nº_pedidos):
        numero = int(input("Introduce numero: "))
        lista.append(numero)
    print(f"La lista ingresada es: {lista}")
    return lista

def suma_lista():
    lista = ingresar_lista()
    return print(sum(lista))

def mayor_lista():
    lista = ingresar_lista()
    return print(max(lista))

"""
def mayor_lista():
    lista = ingresar_lista()
    max = lista[0]
    for numero in lista:
        if numero > max:
            max = numero
        return max
"""

def menor_lista():
    lista = ingresar_lista()
    return print(min(lista))

def menor_lista():
    lista = ingresar_lista()
    min = lista[0]
    for numero in lista:
        if numero < min:
            min = numero
        return min

def media_lista():
    lista = ingresar_lista()
    return print(sum(lista) / len(lista))

def mediana_lista():
    lista = ingresar_lista()
    lista_ordenada = sorted(lista)
    if len(lista_ordenada) % 2 == 0:
        return print(((len(lista) // 2)+(len(lista)// 2 + 1)) / 2 )
    return print(len(lista) // 2 + 1)

def varianza_lista():
    lista = ingresar_lista()
    suma_desviacion = 0
    media = sum(lista) / len(lista)
    for num in lista:
        suma_desviacion += (num - media)**2        
    return print((suma_desviacion) / len(lista))

def desviacion_lista():
    lista = ingresar_lista()
    lista_nueva = []
    promedio = sum(lista) / len(lista)
    for num in lista:
        lista_nueva.append((num-promedio)**2)
    return print((sum(lista_nueva) / len(lista_nueva))**0.5)

def simetria_lista():
    lista = ingresar_lista()
    for i in range(len(lista)//2):
        if lista[i] != lista[len(lista)-1-i]:
            return False
    return True

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def primo_lista():
    lista = ingresar_lista()
    primos = []
    for num in lista:
        if es_primo(num):
            primos.append(num)
    return print(primos)


print("------------------------------------------------")
print("INGRESAR LISTA")

ingresar_lista()

print("------------------------------------------------")
print("SUMA DE NUMEROS")

suma_lista()

print("------------------------------------------------")
print("NUMERO MAYOR EN LISTA")

mayor_lista()

print("------------------------------------------------")
print("NUMERO MENOR EN LISTA")

menor_lista()

print("------------------------------------------------")
print("PROMEDIO DE LISTA")

media_lista()

print("------------------------------------------------")
print("MEDIANA DE LISTA")

mediana_lista()

print("------------------------------------------------")
print("VARIANZA DE LISTA")

varianza_lista()

print("------------------------------------------------")
print("DESVIACION DE LISTA")

desviacion_lista()

print("------------------------------------------------")
print("SIMETRIA DE LISTA")

simetria_lista()

print("------------------------------------------------")
print("NUMEROS PRIMOS EN LISTA")

primo_lista()