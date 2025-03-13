def no_caracteres(caracter):
    numeros = ["1","2","3","4","5","6","7","8","9"]
    return caracter in numeros 

def descripcion():
    print("  |  Contador de  caracter  |")
    print("  |Introduce un . para salir|")
    print("  |  No se aceptan numeros  |")
    print("  | Primer caracter no suma |")
    print("|Solo pon un caracter a la vez|")

def Contador_caracter():
    descripcion()
    caracter_inicial = input("¿Que caracter quieres contar?: ").lower()
    suma = 0
    contador = 0
    while True:
        caracter = input(f"Intoduce caracter {contador+1}: ").lower()
        if no_caracteres(caracter):
            print("Invalido no se aceptan numeros")
            continue
        if caracter == caracter_inicial:
            suma += 1
            contador += 1
        elif caracter == ".":
            print(f"Hay {suma} {caracter_inicial}")
            print("Hasta luego")
            break
        
    
             

Contador_caracter()