# A continuación veréis una serie de enunciados repartidos en bloques por temas.
"""
 Cada bloque contiene entre 2 y 4 ejercicios, cada alumno debe resolver tantos ejercicios de cada 
 bloque según los temas que tenga pendientes siguiendo el siguiente criterio:
 
 - Si tiene suspenso un solo tema, debe resolver TODOS los ejercicios del bloque correspondiente al tema suspenso.
 - Si tiene suspenso el tema 1 y el tema 3, debe resolver dos ejercicios del bloque 1 y dos ejercicios del bloque 3.
 - Si tiene suspenso el tema 1 y el tema 2, debe resolver dos ejercicios del bloque 1 y dos ejercicios del bloque 2.
 - Si tiene suspenso el tema 2 y el tema 3, debe resolver dos ejercicios del bloque 2 y dos ejercicios del bloque 3.
 - Si tiene suspensos los tres temas, debe resolver un ejercicio del bloque 1, otro del bloque 2 y dos del bloque 3.

 Nota: En los casos en los que no se deban resolver todos los ejercicios de un bloque, el alumno/a puede elegir cuáles hacer.
 Atención: En todos los casos deben resolverse 4 ejercicios en total. Para aprobar cada tema, es necesario, 
 al menos, resolver correctamente la mitad de los ejercicios de ese tema. 

 La nota de recuperación de los temas será la nota del examen de recuperación, esta se calculará de forma que cada 
 ejercicio resuelto vale 2.5 puntos.

 Al terminar el examen, el alumno deberá subir el archivo a la plataforma Moodle con el siguiente nombre:
    apellido_nombre_recu1eval.py

    Ejemplo:
    si el alumno se llama Juan Pérez García, el nombre del archivo será:
    perez_garcia_juan_recu1eval.py

    En caso de no seguir este formato, se restarán 10 puntos de la nota final.

A la hora de entregar el examen se deben seguir las siguientes indicaciones:
 - Se deben borrar TODOS los ejercicios que no se hayan resuelto. Tanto el código como el enunciado.
 - De los ejercicios resueltos NO SE PUEDE BORRAR el enunciado ni el código proporcionado.
    - El código proporcionado en los ejercicios NO SE PUEDE MODIFICAR.
"""

# Bloque 1 (Tema 1): 

# Ejercicio 1:
"""
Diseñar un algoritmo que pida al usuario una cadena de texto y un número entero.
El algoritmo debe transformar la cadena de texto de forma que las letras pares se conviertan en mayúsculas y las impares en minúsculas.
Finalmente, el algoritmo debe generar un email con el siguiente formato:
- El número entero introducido por el usuario.
- Un guion bajo.
- La cadena de texto transformada.
- La extensión '@iesdeteis.com'.

Ejemplo de uso:
Introduce una cadena de texto: Hola
Introduce un número entero: 1234

Resultado:
1234_HoLa@iesdeteis.com

Nota: La cadena de texto no puede estar vacía ni ser mayor de 10 caracteres. El número entero debe ser positivo.
 Los datos deben pedirse al usuario hasta que sean correctos.
"""
print("Ejercicio 1 - Email")
cadena = input("Introduce una cadena de texto: ")
numero = int(input("Introduce un número entero: "))
email = ""

# Código del ejercicio 1 aquí




print(email)
print("-"*20)

# Ejercicio 2:
"""
El Yen japonés es la moneda oficial de Japón. El símbolo del yen es ¥.
Un Yen equivale a 0,0062 euros actualmente (Enero de 2025). 
El dolar estadounidense es la moneda oficial de Estados Unidos. El símbolo del dolar es $.
Un dolar equivale a 0,96 euros actualmente (Enero de 2025).
La libra esterlina es la moneda oficial del Reino Unido. El símbolo de la libra es £.
Una libra equivale a 1,18 euros actualmente (Enero de 2025).
Sabiendo estos datos, pide al usuario una cantidad de euros y pregúntale si quiere convertirlos a yenes, dólares o a libras.
Finalmente, muestra al usuario la cantidad de yenes, dolares o libras que tiene tras la conversión.

Nota: La cantidad de euros debe ser positiva. Los datos deben pedirse al usuario hasta que sean correctos.
La moneda a la que se quiere convertir debe ser una de las indicadas, en caso contrario, se volverá a pedir al usuario.
Para pedir el tipo de moneda se puede pedir al usuario que introduzca el nombre de la misma o un número asociado a ella pero nunca el símbolo de la moneda.
"""
print("Ejercicio 2 - Conversor de moneda")
euros = float(input("Introduce una cantidad de euros: "))
moneda = input("¿A qué moneda quieres convertir (yenes, dólares o libras)?: ")

# Código del ejercicio 2 aquí
if euros < 0:
    while True:
        print("No puede ser negativo el dato")
        euros = float(input("Introduce una cantidad de euros: "))
        moneda = input("¿A qué moneda quieres convertir (yenes, dólares o libras)?: ").capitalize()
        if euros > 0:
            match moneda:
                case "yenes":
                    print(f"La cantidad de {euros} euros a yenes es de {euros*0.0062}")
                    break
                case "dolares" | "dólares":
                    print(f"La cantidad de {euros} euros a dolares es de {euros*0.96}")
                    break
                case "libras":
                    print(f"La cantidad de {euros} euros a libras es de {euros*1.18}")
                    break
                case _:
                    print("Solo puedes cambiar a yenes,dolares o libras")
                    break
else:
     match moneda:
        case "yenes":
            print(f"La cantidad de {euros} euros a yenes es de {euros*0.0062}")
            
        case "dolares" | "dólares":
            print(f"La cantidad de {euros} euros a dolares es de {euros*0.96}")
          
        case "libras":
            print(f"La cantidad de {euros} euros a libras es de {euros*1.18}")
         
        case _:
            print("Solo puedes cambiar a yenes,dolares o libras")
            


print("-"*20)

# Bloque 2 (Tema 2):

# Ejercicio 1:
"""
Diseñar una función que reciba un número entero como parámetro y devuelva si este número es primo o no lo es.
Una vez realizada esta función, crea otra que reciba un número entero como parámetro e imprima por pantalla lo siguiente:
- La suma de los números primos menores que el número recibido (sin incluirlo).
- La cantidad de números primos menores que el número recibido (sin incluirlo).
- La media de los números primos menores que el número recibido (sin incluirlo).

Nota: En caso de que el número recibido en la segunda función sea menor o igual a 2, se debe imprimir un mensaje de error.
"""
def es_primo(numero: int) -> bool:
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def datos_primos(numero: int):
    numeros = []
    for i in range (1, numero):
        if es_primo(i):
            numeros.append(i)
    promedio = sum(numeros) / len(numeros) 
    resultado = (f"Suma: {sum(numeros)}, Cantidad: {len(numeros)}, Promedio: {promedio}")
    return resultado

print("Ejercicio 1 - Números primos")
print(es_primo(7)) # True
print(es_primo(10)) # False
datos_primos(10) # Suma: 17, Cantidad: 4, Media: 2.5
datos_primos(20) # Suma: 77, Cantidad: 8, Media: 9.625
datos_primos(2) # Número no válido
print("-"*20)

# Ejercicio 2:
"""
Diseñar una función que dado un número entero, devuelva el mes correspondiente a ese número o None en caso de que no exista un mes para ese número.
Diseñar una función que reciba una lista de ingresos mensuales y otra de gastos mensuales de una empresa.
La función debe imprimir por pantalla el beneficio total de la empresa y el mes en el que se ha obtenido el mayor beneficio.
Además, debe devolver una lista con los nombres de los meses en los que se ha obtenido un beneficio negativo. 
Nota: Las listas de ingresos y gastos deben tener la misma longitud y esta longitud debe ser igual a 12.
En caso de que no sea así, se debe devolver una lista vacía e imprimir un mensaje de error.
"""

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

def mes(numero: int) -> str:
    match numero:
        case 1:
            return "Enero"
        case 2:
            return "Febrero"
        case 3:
            return "Marzo"
        case 4:
            return "Abril"
        case 5:
            return "Mayo"
        case 6:
            return "Junio"
        case 7:
            return "Julio"
        case 8:
            return "Agosto"
        case 9:
            return "Septiembre"
        case 10:
            return "Octubre"
        case 11: 
            return "Noviembre"
        case 12:
            return "Diciembre"
        case _:
            return None
            
def beneficio(ingresos: list, gastos: list) -> list:
    resultado = []
    if len(ingresos) != len(gastos):
        print("Las listas no coinciden")
    elif len(ingresos) > 12 and len(gastos) > 12:
        print("Las listas no pueden tener mas de 12 elementos")
    else:
        for i in ingresos:
            for j in gastos:
                pass
            
        
            
            

print("Ejercicio 2 - Beneficios")
print(mes(1)) # Enero
print(mes(700))
print(mes(13)) # None
ingresos = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000]
gastos = [500, 1000, 1500, 2000, 8000, 8000, 3500, 4000, 4500, 5000, 5500, 6000]
print(beneficio(ingresos, gastos)) # ['Mayo', 'Junio'] además de imprimir el beneficio total (28500) y el mes con mayor beneficio (Diciembre)
gastos.append(1000)
print(beneficio(ingresos, gastos)) # [] además de imprimir un mensaje de error
print("-"*20)

