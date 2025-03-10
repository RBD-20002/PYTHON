def factorial(num1):
    factorial = 1
    for i in range(1,num1+1):
        factorial *= i
    return factorial

def numero_euler(num1):
    suma = 0
    for i in range(num1):
        suma += 1 / factorial(i)
    return suma

def herramienta():
    print("Calculadora euler")
    print("Si quieres salir introduce 0")

def main():
    while True:
        herramienta()
        num1 = int(input("Introduce un numero: "))
        if num1 != 0:
            print(numero_euler(num1))
        elif num1 == 0:
            print("Hasta luego")
            break

main()