import random
print("-"*30+"IDENTIFICAR TU RANGO DE EDAD")

edad = int(input("Introduce tu edad: "))
if edad < 0:
    print("Edad invalida")
elif edad >= 0 and edad <= 12:
    print("Eres un niño")
elif edad >= 13 and edad <= 18:
    print("Eres un adolescente")
elif edad >= 19 and edad <= 30:
    print("Eres un joven")
elif edad >= 31 and edad <= 60:
    print("Eres un adulto")
elif edad >= 61 and edad <= 100:
    print("Eres un adulto mayor")
else:
    print("Eres un cadaver")
    
print("-"*30+"CALCULAR PRECIO DEL VIAJE")

tipoOk = False
while not tipoOk:
    tipo_vehiculo = input("Introduce el tipo de vehiculo: ").capitalize()
    if tipo_vehiculo not in ["Coche","Avion","Tren"]:
        print("Tipo de vehiculo invalido")
        print("Solo puedes viajar en Coche, Avion o Tren")
    else:
        tipoOk = True
        print("Tipo de vehiculo correcto")

distancia = int(input("Introduce la distancia a recorrer: "))

match tipo_vehiculo:
    case "Coche":
        coste = distancia * 0.50
        print("El coste del viaje en coche es de",coste)
    case "Avion":
        coste = distancia * 0.20
        print("El coste del viaje en avion es de",coste)
    case "Tren":
        coste = distancia * 0.30
        print("El coste del viaje en tren es de",coste)
    
print("-"*30+"3")

numero_adivinar = random.randint(1000,9999)

"""while True:
    numero = int(input("Introduce un numero de 4 cifras: "))
    if numero != numero_adivinar:
        print("Has fallado, intenta otra vez")
        if numero in range():
            print("Estas cerca, intenta otra vez")
    else:
        print(f"Has acertado, era {numero_adivinar}")
        break"""
    
print("-"*30+"CALCULAR PROMEDIO DE NOTAS")

notas = []
aprobados  = []
desaprobados = []

nº_pedidos = int(input("Itroduce cuantas notas habra: "))

for i in range(nº_pedidos):
    nota = float(input("Introduce nota: "))
    notas.append(nota)
print(f"Las notas ingresadas son: {notas}")

for i in range(len(notas)):
    if notas[i] >=5:
        aprobados.append(notas[i])
    else:
        desaprobados.append(notas[i])
print(f"Los aprobados son: {aprobados} y los desaprobados son: {desaprobados}")

print("-"*30+"5")

"""Crea un programa que simule un cajero automático. 
El programa debe solicitar la cantidad de dinero que se desea 
retirar y verificar si hay suficiente dinero en la cuenta. 
Si hay suficiente dinero, el programa debe restar la cantidad 
solicitada de la cuenta y mostrar el nuevo saldo. 
Si no hay suficiente dinero, el programa debe mostrar un mensaje de error."""

print("-"*30+"PROMEDIO DE NUMEROS ALEATORIOS")

n_numeros = int(input("Introduce cuantos numeros aleatorios habra: "))
numeros = [random.randint(0,20) for i in range(n_numeros)]
print(f"Los numeros aparecidos son: {numeros}")
promedio = sum(numeros) / len(numeros)
print("El promedio de los numeros es:",promedio)    


print("-"*30+"CALIFICAR ALUMNOS")

nº_alumnos = int(input("Introduce a cuantos alumnos se calificara: "))
for i in range(0,nº_alumnos+1):
    nota = float(input("Introduce la nota del alumno: "))
    if nota >= 70  and nota <= 100:
        print("Aprobado")
    elif nota >= 0 and nota <= 69:
        print("Reprobado")
    else:
        print("Nota invalida")
        
"""Ejercicio 9: Simular un reloj

Crea un programa que simule un reloj.
El programa debe mostrar la hora actual y permitir al usuario 
avanzar o retroceder la hora en una cantidad determinada.."""

print("-"*30+"AREA DE UN TRIANGULO")

base = float(input("Introduce la base del triangulo: "))
altura = float(input("Introduce la altura del triangulo: "))
area = (base * altura) / 2

print(f"El area del triangulo es: {area}")