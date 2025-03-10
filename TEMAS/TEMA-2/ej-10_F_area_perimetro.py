import math

def menu():
    print("|CALCULO DE AREA Y PERIMETRO|")
    print("|1. Rectangulo              |")
    print("|2. Circunferencia          |")
    print("|3. Cuadrado                |")
    print("|4. Triangulo               |")
    print("|5. Salir                   |")

def area_perimetro_rectangulo():
    base = int(input("Introduce el valor de la base: "))
    altura = int(input("Introduce el valor de la altura: "))
    area_rectangulo = base * altura
    perimetro_rectangulo = 2 * (base + altura)
    return print(f"El area del rectangulo es {area_rectangulo} y el perimetro es {perimetro_rectangulo}")

def area_perimetro_circunferencia():
    radio = int(input("Introduce el valor del radio: "))
    area_circunferencia = math.pi * (radio**2)
    perimetro_circunferencia = 2 * math.pi * radio
    return print(f"El area de la circunferencia es {area_circunferencia} y el perimetro es {perimetro_circunferencia} ")

def area_perimetro_cuadrado():
    lado = int(input("Introduce el valor del lado: "))
    area_cuadrado = lado ** 2
    perimetro_cuadrado = 4 * lado 
    return print(f"El area del cuadrado es {area_cuadrado} y el perimetro es {perimetro_cuadrado}")

def area_perimetro_triangulo_equilatero():
    lado = int(input("Introduce el valor del lado: "))
    area_triangulo_equilatero = (math.sqrt(3) / 4) * (lado ** 2)
    perimetro_triangulo_equilatero = 3 * lado 
    return print(f"El area del triangulo equilatero es {area_triangulo_equilatero} y el perimetro es {perimetro_triangulo_equilatero}")

def calculos(opcion):
    match opcion:
        case "1":
            return area_perimetro_rectangulo(base,altura)
        case "2":
            return area_perimetro_circunferencia(radio)
        case "3":
            return area_perimetro_cuadrado(lado)
        case "4":
            return area_perimetro_triangulo_equilatero(lado)
        case "5":
            return print("Hasta luego")

def validar_calculos(opcion):
    return opcion in ["1" , "2" , "3" , "4" , "5"]

def calculador_figuras():
    menu()
    opcion = input("Introduce la opcion de la figura que quieres calcular: ")
    while opcion != "5":
        if not validar_calculos(opcion):
            print("opcion invalida")
            menu()
            opcion = input("Introduce la opcion de la figura que quieres calcular: ")
            continue
        if opcion == "1":
            print(area_perimetro_rectangulo())
        if opcion == "2":
            print(area_perimetro_circunferencia())
        if opcion == "3":
                print(area_perimetro_cuadrado())
        if opcion == "4":
            print(area_perimetro_triangulo_equilatero())
        menu()
        opcion = input("Introduce la opcion de la figura que quieres calcular: ")
    print("HASTA LUEGO")
                
       
calculador_figuras()