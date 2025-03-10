"""Diseñar un algoritmo que pida al usuario un número del 1 al 9 y le conteste diciendo si el 
número es primo o no.  Por ejemplo, si introduce el  7, le responderá que es primo."""
numero = int(input("Introduce un numero: "))
if numero <= 1:
    print("El número no es primo")
else:
    es_primo = True
    for i in range(2, int(numero**0.5)+1):
        if numero % i == 0:
            es_primo = False 
    if es_primo:
        print("El numero es primo")
    else:
        print("El número no es primo")