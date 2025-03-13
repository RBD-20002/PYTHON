print("-"*50)

"""Ejercicio 1: Funciones y listas
Enunciado: Diseña una función que reciba el nombre de un país y devuelva su capital. 
La función debe aceptar el nombre del país en minúsculas, mayúsculas o combinando ambas. 
Si el país no existe, la función debe devolver None.
Los países y sus capitales son los siguientes:
España: Madrid
Francia: París
Italia: Roma
Alemania: Berlín
Japón: Tokio
Una vez creada esta función, crea otra que use la lista de países dada (paises) y devuelva una string con el nombre de cada país y su capital. 
Si un país no existe, se debe indicar que no existe de la siguiente manera: "Marte: no es un país".
El formato de la string debe ser el siguiente:
España: Madrid, Francia: París, Marte: no es un país"""

paises = ["ESPAÑA", "FRANCIA", "MARTE", "ITALIA", "JAPON"]

def capital_pais(pais: str) -> str:
    pais = pais.capitalize()
    match pais:
        case "España":
            return (f"{pais}: Madrid")
        case "Francia":
            return (f"{pais}: Paris")
        case "Italia":
            return (f"{pais}: Roma")
        case "Alemania":
            return (f"{pais}: Berlin")
        case "Japon":
            return (f"{pais}: Tokio")
        case _:
            return (f"{pais}: no es un país")

def capitalPaises(paises: list) -> str:
    lista = []
    for i in range(len(paises)):
        lista.append(capital_pais(paises[i]))
    return ", ".join(lista)
       
print(capitalPaises(paises))


print("-"*50)


"""Ejercicio 2: Manipulación de strings
Enunciado: Diseña una función que reciba un número entero y devuelva una pirámide de 
números en forma de string. La pirámide debe tener la siguiente forma:"""
# para 3:
1
22
333
22
1

# para 5:
1
22
333
4444
55555
4444
333
22
1


def piramideNumeros(numero: int) -> str:
    piramide = ""
    for i in range(1, numero + 1):
        piramide += str(i) * i + "\n"
    for i in range(numero - 1, 0, -1):
        piramide += str(i) * i + "\n"
    return piramide

print(piramideNumeros(3))


print("-"*50)


"""Ejercicio 3: Funciones y listas
Enunciado: Diseña una función que reciba una temperatura en grados Celsius y devuelva la clasificación correspondiente:

Menos de 0: Congelante
0-15: Frío
16-25: Templado
26-35: Caluroso
Más de 35: Extremadamente caluroso
La función debe devolver un string con la clasificación. Si la temperatura no es un número, la función debe devolver None.

Una vez creada esta función, crea otra que reciba dos listas: una con los nombres de las ciudades y otra con las 
temperaturas de esas ciudades. La función debe devolver una lista con el nombre de cada ciudad y su clasificación. Si las listas no tienen la misma longitud, 
la función debe devolver una lista con un solo elemento que sea Error: Las listas no tienen la misma longitud"""

ciudades = ["Madrid", "Barcelona", "Valencia", "Sevilla"]
temperaturas = [12, 28, 35, 40]

def clasificacionTemperatura(temp) -> str:
    if not isinstance(temp,(int,float)):
        return None
    elif temp < 0:
        return "Congeleante"
    elif 0 <= temp <= 15:
        return "Frio"
    elif 16 <= temp <= 25:
        return "Templado"
    elif 26 <= temp <= 35:
        return "Caluroso"
    elif temp > 35:
        return "Extremadamente Caluroso"
        
print(clasificacionTemperatura(12.5)) # Frio
print(clasificacionTemperatura("Dace"))

def clasificacionCiudades(ciudades: list, temperaturas: list) -> list:
    if len(ciudades) != len(temperaturas):
        return "ERROR: Las listas no tiene la misma longitud"
    else:
        resultado = []
        for ciudad, temperatura in zip(ciudades, temperaturas):
            clasificacion = clasificacionTemperatura(temperatura)
            resultado.append(f"{ciudad}: {clasificacion}")
        return resultado
            
print(clasificacionCiudades(ciudades, temperaturas))


print("-"*50)


"""Ejercicio 5: Funciones y strings
Enunciado: Diseña una función que reciba una palabra y devuelva True si es un palíndromo (se lee igual de izquierda 
a derecha que de derecha a izquierda) y False en caso contrario. La función debe ignorar mayúsculas y minúsculas."""

def esPalindromo(palabra: str) -> bool:
    if palabra == palabra[::-1]:
        return True
    else:
        return False
    
print(esPalindromo("oso"))  # True
print(esPalindromo("hola"))  # False


print("-"*50)


"""Ejercicio 6: Funciones y listas
Enunciado: Diseña una función que reciba el nombre de un planeta y devuelva su distancia promedio al Sol en millones de kilómetros. 
La función debe aceptar el nombre del planeta en minúsculas, mayúsculas o combinando ambas. 
Si el planeta no existe, la función debe devolver None.

Los planetas y sus distancias al Sol son los siguientes:
Mercurio: 57.9
Venus: 108.2
Tierra: 149.6
Marte: 227.9
Júpiter: 778.5
Saturno: 1433.5
Urano: 2872.5
Neptuno: 4495.1

Una vez creada esta función, crea otra que use la lista de planetas dada (planetas) y devuelva una cadena 
con el nombre de cada planeta y su distancia al Sol. Si un planeta no existe, 
se debe indicar que no existe de la siguiente manera: "Plutón: no es un planeta".
El formato de la cadena debe ser el siguiente:
Mercurio: 57.9, Venus: 108.2, Plutón: no es un planeta"""

planetas = ["Mercurio", "Venus", "Pluton", "Marte", "Francia"]

def distancia_planetaria(planeta: str):
    planetas = planeta.capitalize()
    match planetas:
        case "Mercurio":
            return 57.9
        case "Venus":
            return 108.2
        case "Tierra":
            return 149.6
        case "Marte":
            return 227.9
        case "Jupiter":
            return 778.5
        case "Saturno":
            return 1433.5
        case "Urano":
            return 2872.5
        case "Neptuno":
            return 4495.1
        case "Pluton":
            return "No es un planeta"
        case _:
            return None

print(distancia_planetaria("MartE"))  # 227.9
print(distancia_planetaria("Francia"))  # None
print(distancia_planetaria("Pluton"))  # No es un planeta

def lista_planetas(planetas: list):
    resultado = []
    for i in planetas:
        resultado.append(f"{i}: {distancia_planetaria(i)}")
    return ", ".join(resultado)

print(lista_planetas(planetas))


print("-"*50)


"""Ejercicio 7: Funciones y listas
Enunciado:Diseña una función que reciba una lista de números enteros y devuelva una 
lista con los números pares multiplicados por 2 y los números impares multiplicados por 3.

Por ejemplo:
Para la lista [1, 2, 3, 4, 5], la función debe devolver [3, 4, 9, 8, 15]

Una vez creada esta función, crea otra que reciba dos listas: una con los nombres de 
los estudiantes y otra con sus calificaciones (números enteros).
La función debe devolver una lista con el nombre de cada estudiante y su calificación transformada 
según la función anterior. Si las listas no tienen la misma longitud, la función debe devolver 
una lista con un solo elemento que sea: 
Error: Las listas no tienen la misma longitud"""

numeros = [1, 2, 3, 4, 5]
alumnos = ["ricardo","jacqueline","jose","nicolas","jeff"]

def numeros_multiplicados(numeros: list):
    resultado = []
    for i in numeros:
        if i % 2 == 0:
            resultado.append(i * 2)
        else:
            resultado.append(i * 3)
    return resultado

print(numeros_multiplicados(numeros))

def numeros_notas(numeros: list , alumnos: list):
    resultado = [] 
    if len(numeros) != len(alumnos):
        return "ERROR: Las listas de las notas no coinciden con los alumons"
    else:
        for i in range(len(numeros)):
            resultado.append(f"{alumnos[i]}: {numeros_multiplicados(numeros)[i]}")
        return resultado
    
print(numeros_notas(numeros, alumnos))   
