"""
Diseña una función que reciba el nombre de un planeta del Sistema Solar y devuelva un diccionario con sus características.
Las características son:
- Número de lunas
- Distancia media al Sol (en millones de km)
- Composición (rocoso o gaseoso)

La función debe devolver un diccionario con las características del planeta. Si el planeta no existe, la función debe devolver None.

Los datos de los planetas son los siguientes:
- Mercurio: (0, 57.91, 'rocoso')
- Venus: (0, 108.21, 'rocoso')
- Tierra: (1, 149.6, 'rocoso')
- Marte: (2, 227.92, 'rocoso')
- Júpiter: (79, 778.57, 'gaseoso')
- Saturno: (82, 1433.5, 'gaseoso')
- Urano: (27, 2872.5, 'gaseoso')
- Neptuno: (14, 4495.1, 'gaseoso')
- Plutón: (5, 5906.4, 'rocoso')

Una vez creada esta función, se debe crear otra que use un conjunto de planetas dados y devuelva una string con el nombre de cada planeta y sus características.
Si un planeta no existe, se debe indicar que no existe de la siguiente manera: "Alderaan: no existe en el Sistema Solar".        
El formato de la string debe ser el siguiente:
"Mercurio: 0 lunas, 57.91 millones de km, rocoso, Tierra: 1 luna, 149.6 millones de km, rocoso, Alderaan: no existe en el Sistema Solar".
"""

planetas_info = {
    "mercurio": (0, 57.91, 'rocoso'),
    "venus": (0, 108.21, 'rocoso'),
    "tierra": (1, 149.6, 'rocoso'),
    "marte": (2, 227.92, 'rocoso'),
    "jupiter": (79, 778.57, 'gaseoso'),
    "saturno": (82, 1433.5, 'gaseoso'),
    "urano": (27, 2872.5, 'gaseoso'),
    "neptuno": (14, 4495.1, 'gaseoso'),
    "pluton": (5, 5906.4, 'rocoso')
}

def caracteristicas_planeta(planeta: str) -> dict:
    planeta = planeta.lower()
    if planeta in planetas_info:
        lunas, distancia, composicion = planetas_info[planeta]
        return {
            "lunas": lunas,
            "distancia": distancia,
            "composicion": composicion
        }
    return None

def mostrar_info_planeta(planeta: str) -> None:
    info = caracteristicas_planeta(planeta)
    if info is None:
        print(f"{planeta.capitalize()}: no existe en el Sistema Solar")
    else:
        if info['lunas'] == 1:
            print(f"{planeta.capitalize()}: {info['lunas']} luna, {info['distancia']} millones de km, {info['composicion']}")
        else:
            print(f"{planeta.capitalize()}: {info['lunas']} lunas, {info['distancia']} millones de km, {info['composicion']}")

def caracteristicas_planetas(planetas: set) -> None:
    for planeta in planetas:
        mostrar_info_planeta(planeta)

# Ejemplo de uso
planetas_set = {"MERCURIO", "VENUS", "TIERRA", "ALDERAAN", "JUPITER", "MARTE"}
caracteristicas_planetas(planetas_set)

# Ejemplo de uso para un planeta específico
mostrar_info_planeta("neptuno")  # Muestra la información de Neptuno
mostrar_info_planeta("cochez")    # Muestra que no existe en el Sistema Solar

print("-"*50)

coches_info = {
    "ford mustang": ('Ford', 'Mustang', 2021, 55),
    "tesla model s": ('Tesla', 'Model S', 2022, 95),
    "chevrolet camaro": ('Chevrolet', 'Camaro', 2020, 45),
    "honda civic": ('Honda', 'Civic', 2019, 25),
    "bmw m3": ('BMW', 'M3', 2021, 70),
    "audi a4": ('Audi', 'A4', 2022, 50),
    "toyota corolla": ('Toyota', 'Corolla', 2018, 20)
}

def caracteristicas_coche(coche: str) -> dict:
    coche = coche.lower()
    if coche in coches_info:
        marca, modelo, anio, precio = coches_info[coche]
        return {
            "marca": marca,
            "modelo": modelo,
            "anio": anio,
            "precio": precio
        }
    return None

def caracteristicas_coches(coches: set) -> None:
    for coche in coches:
        info = caracteristicas_coche(coche)
        if info is None:
            print(f"{coche.capitalize()}: no existe en el concesionario")
        else:
            print(f"{coche.capitalize()}: {info['marca']}, {info['modelo']}, {info['anio']}, {info['precio']} mil dólares")

# Ejemplo de uso
coches_set = {"Ford Mustang", "Tesla Model S", "Chevrolet Camaro", "CocheX", "BMW M3"}
caracteristicas_coches(coches_set)

print("-"*50)

coches_info = {
    "nissan altima": ('Nissan', 'Altima', 2020, 30),
    "ford f-150": ('Ford', 'F-150', 2021, 45),
    "honda accord": ('Honda', 'Accord', 2019, 35),
    "chevrolet silverado": ('Chevrolet', 'Silverado', 2022, 50),
    "tesla model 3": ('Tesla', 'Model 3', 2022, 60),
    "bmw x5": ('BMW', 'X5', 2021, 70),
    "audi q5": ('Audi', 'Q5', 2020, 55)
}

def caracteristicas_coche(coche: str) -> dict:
    coche = coche.lower()
    if coche in coches_info:
        marca, modelo, anio, precio = coches_info[coche]
        return {
            "marca": marca,
            "modelo": modelo,
            "anio": anio,
            "precio": precio
        }
    return None

def mostrar_info_coche(coche: str) -> None:
    info = caracteristicas_coche(coche)
    if info is None:
        print(f"{coche.capitalize()}: no existe en el concesionario")
    else:
        print(f"{coche.capitalize()}: {info['marca']}, {info['modelo']}, {info['anio']}, {info['precio']} mil dólares")

def caracteristicas_coches(coches: set) -> None:
    for coche in coches:
        mostrar_info_coche(coche)

# Ejemplo de uso
coches_set = {"Nissan Altima", "Ford F-150", "Chevrolet Silverado", "CocheZ", "Tesla Model 3"}
caracteristicas_coches(coches_set)

# Ejemplo de uso para un coche específico
mostrar_info_coche("honda accord")  # Muestra la información de Honda Accord
mostrar_info_coche("cochez")  # Muestra que no existe en el concesionario
"""resultado = caracteristicas_coches(coches_set)
print(resultado)""" #para que devuelva una string como resultado

print("-"*50)

# Información de los alumnos
alumnos_info = {
    "ana torres": {'id': 101, 'nombre': 'Ana', 'apellido': 'Torres', 'edad': 19, 'promedio': 8.5, 'beca': True},
    "luis fernandez": {'id': 102, 'nombre': 'Luis', 'apellido': 'Fernández', 'edad': 21, 'promedio': 7.8, 'beca': False},
    "sofia ramirez": {'id': 103, 'nombre': 'Sofía', 'apellido': 'Ramírez', 'edad': 20, 'promedio': 9.2, 'beca': True},
    "javier ortiz": {'id': 104, 'nombre': 'Javier', 'apellido': 'Ortiz', 'edad': 22, 'promedio': 6.5, 'beca': False},
    "carla gonzalez": {'id': 105, 'nombre': 'Carla', 'apellido': 'González', 'edad': 23, 'promedio': 8.0, 'beca': True},
}

def obtener_info_alumno(alumno: str) -> dict:
    alumno = alumno.lower()
    return alumnos_info.get(alumno, None)

def mostrar_info_alumno(alumno: str) -> None:
    info = obtener_info_alumno(alumno)
    if info is None:
        print(f"{alumno.capitalize()}: no existe en la base de datos")
    else:
        beca_status = "con beca" if info['beca'] else "sin beca"
        print(f"ID: {info['id']}, {info['nombre']} {info['apellido']}: {info['edad']} años, Promedio: {info['promedio']}, {beca_status}")

# Ejemplo de uso
mostrar_info_alumno("ana torres")  # Muestra la información de Ana Torres
mostrar_info_alumno("luis fernandez")  # Muestra la información de Luis Fernández
mostrar_info_alumno("cochex")  # Muestra que no existe en la base de datos