def invertir_lista(lista):
    return print(lista[::-1])

def invertir_lista_2(lista):
    lista_invertida = []
    for i in range(len(lista)-1, -1, -1):
        lista_invertida.append(lista[i])
    print(lista_invertida)

def invertir_lista_3(lista):
    return print(list(reversed(lista)))

lista = [1, 2, 3, 4, 5]
invertir_lista(lista)
invertir_lista_2(lista)
invertir_lista_3(lista)