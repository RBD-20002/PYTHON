print("-"*30+"ADIVINAR NUMERO")
import random

numero_secreto = random.randint(1, 100)
intento = 0
while True:
    intento = int(input("Adivina el número (entre 1 y 100): "))
    match intento:
        case n if n < numero_secreto:
            print("El número es mayor")
        case n if n > numero_secreto:
            print("El número es menor")
        case _:
            print("¡Felicidades! Adivinaste el número")
            break
        
        
print("-"*30+"NUMEROS PRIMOS")


numero = int(input("Ingresa un número: "))
es_primo = True
divisor = 2

while divisor <= numero // 2:
    if numero % divisor == 0:
        es_primo = False
        break
    divisor += 1

if es_primo and numero > 1:
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")

    
print("-"*30+"FACTORIAL DE UN NUMERO")


numero = int(input("Ingresa un número: "))
factorial = 1

for i in range(1, numero + 1):
    factorial *= i

print(f"El factorial de {numero} es: {factorial}")


print("-"*30+"ADIVINAR NUMERO CON INTENTOS")


numero_secreto = random.randint(1, 100)
intentos = 0
adivinado = False

print("Adivina el número secreto entre 1 y 100.")

while not adivinado:
    intento = int(input("Ingresa tu intento: "))
    intentos += 1

    if intento < numero_secreto:
        print("Muy bajo. Intenta de nuevo.")
    elif intento > numero_secreto:
        print("Muy alto. Intenta de nuevo.")
    else:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        adivinado = True
        

print("-"*30+"CONTAR ELEMENTOS DE UNA LISTA")


mi_lista = [2, 4, 6, 8, 10]
contador = 0
while contador < len(mi_lista):
    contador += 1
print(contador)


print("-"*30+"MUlTIPLICAR ELEMENTOS DE UNA LISTA")

multiplicador = int(input("El numero por el cual se multiplicara: "))
mi_lista = [2, 4, 6, 8, 10]
resultado = []
for i in mi_lista:
    resultado.append(i * multiplicador)

print(resultado)


print("-"*30+"INVERTIR UNA LISTA")

# Usando for
mi_lista = [1, 2, 3, 4, 5]
invertida = []
for i in range(len(mi_lista)-1, -1, -1):
    invertida.append(mi_lista[i])
print(invertida)

# Usando while (de otra forma)
mi_lista = [1, 2, 3, 4, 5]
invertida = []
indice = 0

while indice < len(mi_lista):
    invertida.insert(0, mi_lista[indice])  # Inserta al principio de la lista
    indice += 1

print(invertida)


print("-"*30+"ELIMINAR NUMEROS DUPLICADOS DE UNA LISTA")

# Usando while
mi_lista = [1, 2, 2, 3, 4, 4, 5]
resultado = []
indice = 0

while indice < len(mi_lista):
    if mi_lista[indice] not in resultado:
        resultado.append(mi_lista[indice])
    indice += 1

print(resultado)

# Usando for
mi_lista = [1, 2, 2, 3, 4, 4, 5]
resultado = []

for num in mi_lista:
    if num not in resultado:
        resultado.append(num)

print(resultado)
