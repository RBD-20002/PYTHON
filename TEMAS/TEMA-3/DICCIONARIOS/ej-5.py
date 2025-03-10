"""
Escribir una función que reciba un diccionario con los planetas del sistema solar y sus distancias al sol, 
además debe recibir un planeta y devolver su distancia a la Tierra. Las distancias se expresan en millones 
de kilómetros. La distancia de la Tierra al Sol es de 149.6 millones de kilómetros. 
"""
planetas = {"Mercurio": 57.9,
            "Venus": 108.2,
            "Tierra": 149.6,
            "Marte": 227.9,
            "Júpiter": 778.5,
            "Saturno": 1433.4,
            "Urano": 2872.5,
            "Neptuno": 4495.1,
            "Pluton": 5906.4}

def distanciaPlanetaria(planetas:dict , planet:str):
    if planetas:
        for planeta,distancia in planetas.items():
            if planeta.lower() == planet.lower():
                return f"La distancia de {planet} al sol es {distancia}"
    return "El planeta no se encuentra en el sistema solar"

print(distanciaPlanetaria(planetas, "tierra"))
print(distanciaPlanetaria(planetas,"pluton"))

def distancia_a_tierra(planetas:dict , planet:str):
    try:
        return round(abs(planetas[planet] - 149.6),2)
    
    except AttributeError:
        print("ERROR: el diccionario no es valido")
        return None
    except KeyError:
        print("ERROR: planeta no encontrado")
        return -1
    except:
        print("ERROR: fallo inesperado")
        return None
    
print(distancia_a_tierra(planetas, "Marte")) # 78.3
print(distancia_a_tierra(planetas, "Plutón")) # 5756.8
print(distancia_a_tierra(planetas, "Venus")) # 41.4
print(distancia_a_tierra(planetas, "Saturno")) # 1283.8
print(distancia_a_tierra(planetas, "Júpiter")) # 628.9
print(distancia_a_tierra(planetas, "Neptuno")) # 4345.5
print(distancia_a_tierra(planetas, "Urano")) # 2722.9
print(distancia_a_tierra(planetas, "Mercurio")) # 91.7
print(distancia_a_tierra(planetas, "Tierra")) # 0.0
print(distancia_a_tierra(planetas, "Alderaan")) # -1
