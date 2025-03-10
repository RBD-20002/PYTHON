def suma_divisores(num1):
    suma = 0
    for i in range(1,num1//2+1):
        if num1 % i == 0:
            suma += i
    return suma 

def numero_amigos():
    num1 = int(input("Introduce num1: "))
    num2 = int(input("Introduce num2: "))
    if suma_divisores(num1) == num2 and suma_divisores(num2) == num1:
        print("Los numeros son amigos")
    else:
        print("Los numeros no son amigos")


