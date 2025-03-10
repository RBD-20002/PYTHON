print("--------------------------------CONTAR DIGITOS")
def contar_digitos(n):
    if n < 10:
        return 1
    else:
        return 1 + contar_digitos(n // 10)

print(contar_digitos(12345))

print("--------------------------------FIBONACCI")
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

numero = 6
print(f"El {numero}º número de Fibonacci es {fibonacci(numero)}")

print("--------------------------------INVERTIR CADENA")
def invertir(cadena):
    if len(cadena) == 0:
        return cadena
    return invertir(cadena[1:]) + cadena[0]

texto = "palindromo"
print(f"La cadena invertida es: {invertir(texto)}")

print("--------------------------------LONGITUD LISTA")
def longitud(lista):
    if lista == []:
        return 0
    else:
        return 1 + longitud(lista[1:])

print(longitud([1, 2, 3, 4, 5]))

print("--------------------------------POTENCIA NUMERO")
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

print(potencia(2, 3))

print("--------------------------------SUMA LISTA")
def suma_lista(lista):
    if len(lista) == 0:
        return 0
    return lista[0] + suma_lista(lista[1:])

lista = [1, 2, 3, 4, 5]
print(f"La suma de los elementos es: {suma_lista(lista)}")

print("--------------------------------SUMA PRIMEROS NUMEROS")
def suma_primeros_numeros(numero):
    if numero == 0:
        return 0
    return numero + suma_primeros_numeros(numero-1)

suma_primeros_numeros(4)

print("--------------------------------TORRE HANOI")
def torre_de_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco {n} desde {origen} hasta {destino}")
    else:
        torre_de_hanoi(n - 1, origen, auxiliar, destino)
        print(f"Mover disco {n} desde {origen} hasta {destino}")
        torre_de_hanoi(n - 1, auxiliar, destino, origen)

torre_de_hanoi(3, 'A', 'C', 'B')

print("--------------------------------NUMERO BINARIO")
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

print(decimal_a_binario(3.4))

print("--------------------------------MULTIPLICACION")
def multiplicar(a, b):
    if b == 0:
        return 0
    elif b > 0:
        return a + multiplicar(a, b - 1)
    else:
        return - multiplicar(a, -b)

print(multiplicar(5, 3))

print("--------------------------------NUMERO MAYOR EN LISTA")
def hallar_maximo(lista):
    if len(lista) == 1:
        return lista[0]
    return max(lista[0], hallar_maximo(lista[1:]))

print(hallar_maximo([5, 10, 3, 8, 2]))

print("--------------------------------NUMERO MENOR EN LISTA")
def hallar_minimo(lista):
    if len(lista) == 1:
        return lista[0]
    return min(lista[0], hallar_minimo(lista[1:]))

print(hallar_minimo([99,54,1,4,7,0.2]))

print("--------------------------------FACTORIAL")
def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(int(n) - 1)

print(factorial(5))

print("--------------------------------IMPRIMERO DE 1 A N")
def imprimir_1_a_n(n, actual=1):
    # Caso base: si actual supera a n, terminamos la recursión
    if actual > n:
        return
    if actual == n:
        print(actual)
    else:
        print(actual, end=" ")
    imprimir_1_a_n(n, actual + 1)
    
imprimir_1_a_n(4)

print("--------------------------------PALINDROMO")
def es_palindromo(palabra: str) -> bool:
    # Caso base: Si la longitud de la palabra es 0 o 1, es un palíndromo
    if len(palabra) <= 1:
        return True
    # Comprobar si los extremos son iguales
    if palabra[0] != palabra[-1]:
        return False
    # Llamada recursiva con la palabra sin los extremos
    return es_palindromo(palabra[1:-1])

print(es_palindromo("radar"))

print("--------------------------------BUSCAR EN TUPLAS")
def recursivtup(tup: tuple, search):
    if len(tup) == 0:
        return False
    if isinstance(tup[-1], tuple):
        for i in tup[-1]:
            if i == search:
                return True
    else:
        if tup[-1] == search:
            return True
    return recursivtup(tup[0:-1], search)

print(recursivtup((1, 2, 3, (1, "este"), 4), "esta"))

print("--------------------------------MCD")
def MCD(a: int, b: int) -> int:
    if b == 0:
        return a
    if b != 0:
        return MCD(b, a % b)

print(MCD(48, 18))

print("--------------------------------INVERTIR TEXTO")
def invertir(cadena: str) -> str:
    if len(cadena) == 0:
        return " "
    if len(cadena) > 0:
        return cadena[-1] + invertir(cadena[:-1])

print(invertir("python"))

print("--------------------------------CONTADOR DE CEROS")
def contar_ceros(numero: int) -> int:
    numero = abs(numero)
    if numero == 0:
        return 1  
    if numero < 10:
        return 0  
    ultimo_digito = numero % 10
    ceros_en_resto = contar_ceros(numero // 10)
    return ceros_en_resto + (1 if ultimo_digito == 0 else 0)

print(contar_ceros(102030))

print("--------------------------------COMBINACIONES POSIBLES EN UNA LISTA")
def generar_combinaciones(lista):
    if not lista:
        return [[]]
    primer_elemento = lista[0]
    combinaciones_sin_primero = generar_combinaciones(lista[1:])
    combinaciones_con_primero = [combinacion + [primer_elemento] for combinacion in combinaciones_sin_primero]
    return combinaciones_sin_primero + combinaciones_con_primero

lista = [1, 2,3,4]
print("Combinaciones posibles:", generar_combinaciones(lista))

print("--------------------------------CONTEO DE LISTAS EN LISTAS")
def numero_listas(lista: list) -> int:
    if lista == []:
        return 0
    return 1 + numero_listas(lista[1:])

listas = [[1,2,3], [4,5,6], [7,8,9]]
print(numero_listas(listas))

print("--------------------------------CANTIDAD DE LOS ELEMENTOS EN LA LISTA MAS GRANDE")
def elementos_lista_mas_larga(lista: list) -> int:
    if lista == []:
        return 0
    return max(len(lista[0]), elementos_lista_mas_larga(lista[1:]))

listas = [[1,2,3], [4,5,6,10], [7,8,9]]
print(elementos_lista_mas_larga(listas))

print("--------------------------------INVERITR LISTA")
def invertir_lista(lista: list) -> list:
    if lista == []:
        return []
    return invertir_lista(lista[1:]) + [lista[0]]

listas = [1,2,34,5,4,4,9]
print(invertir_lista(listas))

print("--------------------------------TABLA DE MULTIPLICAR")
def tabla_multiplicar(numero: int) -> int:
    try:
        if numero == 0:
            return 0
        return f"{numero} x {numero} = {numero * numero}\n{tabla_multiplicar(numero - 1)}"
    except RecursionError:
        return "Número demasiado grande."
    
print(tabla_multiplicar(5))