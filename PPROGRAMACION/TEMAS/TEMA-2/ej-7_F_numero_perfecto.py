def descripcion():
    print("   |Numero perfecto|   ")
    print("|Solo  acepta positivos|")
    print("|Introduce 0 para salir|")

def suma_divisores(num1):
    suma = 0 
    for i in range(1,num1):
        if num1 % i == 0:
            suma += i
    return suma

def numero_perfecto():
    suma = 0
    while True:
        descripcion()
        num1 = int(input("Introduce num1: "))
        if num1 < 0:
            print("El numero debe ser positivo")
            continue
        if num1 == 0:
            print("ADIOS")
            break
        if suma_divisores(num1) == num1:
            print("El numero es perfecto")
        else: 
            print("El numero no es perfecto")

numero_perfecto()