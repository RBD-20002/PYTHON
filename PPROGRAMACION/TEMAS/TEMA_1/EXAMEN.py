print("-----------------------------1")

while True:
    propina = input("Introduce como fue el servicio: ").lower()
    if propina == "adios":
        print("Adios")
        break
    elif propina == "bueno":
        cuenta = int(input("Introduce tu cuenta: "))
        print(f"La cuenta es: {cuenta} y la propina seria: {cuenta*0.20} y el total seria {cuenta+(cuenta*0.20)}")
    elif propina == "regular":
        cuenta = int(input("Introduce tu cuenta: "))
        print(f"La cuenta es: {cuenta} y la propina seria: {cuenta*0.15} y el total seria {cuenta+(cuenta*0.15)}")
    elif propina == "malo":
        cuenta = int(input("Introduce tu cuenta: "))
        print(f"La cuenta es: {cuenta} y la propina seria: {cuenta*0.05} y el total seria {cuenta+(cuenta*0.10)}")
    elif propina != "bueno,regular,malo":
        print("Opcion invalida debe ser:(bueno,regular,malo)")

print("-----------------------------2")

palabra = input("Introduce una palabra: ")
if palabra == palabra[::-1]:
    print("La palabra es un palindromo")

print("-----------------------------3")

dia_actual = 10
mes_actual = 11
año_actual = 2024

dia_nacimiento = int(input("Introduce tu dia de nacimiento: "))
mes_nacimiento = int(input("Introduce tu mes de nacimiento: "))
año_nacimiento = int(input("Introduce tu año de nacimiento: "))

if (mes_actual == mes_nacimiento and dia_actual < dia_nacimiento):
    edad = (año_actual - año_nacimiento) + 1
    print(edad)
else:
    edad = año_actual - año_nacimiento
    print(edad)

print("-----------------------------4")

altura = int(input("Introduce la altura del rombo: "))
if altura % 2 == 0:
    print("La altura debe ser impar")
for i in range((altura//2) + 1):
    print(" " * ((altura//2) - i) + "*" + " " * (2 * i - 1) + ("*" if i > 0 else ""))
for i in range((altura//2) - 1, -1, -1):
    print(" " * ((altura//2) - i) + "*" + " " * (2 * i - 1) + ("*" if i > 0 else ""))

print("-----------------------------5")

#WHILE:
suma_digitos = 0
numero = int(input("Introduce un numero: "))
while numero > 0:
    digito = numero % 10
    numero //= 10
    suma_digitos += digito
print(suma_digitos)

#FOR:
suma_digitos = 0
numero = int(input("Introduce un numero entero: "))
for i in range(len(str(numero))):
    digito = numero % 10
    numero //= 10
    suma_digitos += digito
print(f"La suma de los digitos es: {suma_digitos}")
