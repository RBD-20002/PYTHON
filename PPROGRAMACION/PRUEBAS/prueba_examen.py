# Haz una funcion que pida al usuario los datos de un coche, los datos son:
"""
Marca - string
Color - string
Cilindrada - entero
"""

def diccionarioVehiculo():
    diccionario = {}
    diccionario["marca"] = input("Introduce la marca del coche: ")
    diccionario["modelo"] = input("Introduce el modelo del coche: ")
    diccionario["color"] = input("Introduce el color del coche: ")
    cilindradaok = False
    while not cilindradaok:
        try:
            diccionario["cilindrada"] = float(
                input("Introduce la cilindrada del coche: "))
            if cilindradaok < 0:
                print("Error: la cilindrada debe ser un número positivo")
                raise AttributeError(
                    "Error: la cilindrada debe ser un número positivo")
            cilindradaok = True
        except AttributeError as e:
            print(e)
        except ValueError:
            print("Error: la cilindrada debe ser un número")
        return diccionario

# o poniendo arriba por ejemplo solo color = input y en el return {"Marca": marca, "Color": color, "Cilindrada": cilindrada}
"""print(diccionarioVehiculo())"""

def diccionarioVehiculo2():
    marca = input("Introduce la marca del coche: ")
    if marca == "":
        print("Error: la marca no puede estar vacía")
        raise AttributeError("Error: la marca no puede estar vacía")
    if not isinstance(marca, str):
        print("Error: la marca debe ser un string")
        raise AttributeError("Error: la marca debe ser un string")
    modelo = input("Introduce el modelo del coche: ")
    if modelo == "":
        print("Error: el modelo no puede estar vacío")
        raise AttributeError("Error: el modelo no puede estar vacío")
    if not isinstance(modelo, str):
        print("Error: el modelo debe ser un string")
        raise AttributeError("Error: el modelo debe ser un string")
    color = input("Introduce el color del coche: ")
    if color == "":
        print("Error: el color no puede estar vacío")
        raise AttributeError("Error: el color no puede estar vacío")
    if not isinstance(color, str):
        print("Error: el color debe ser un string")
        raise AttributeError("Error: el color debe ser un string")
    cilindrada = int(input("Introduce la cilindrada del coche: "))
    cilindradaok = False
    while not cilindradaok:
        try:
            cilindrada = float(cilindrada)
            if cilindrada < 0:
                print("Error: la cilindrada debe ser un número positivo")
                raise AttributeError(
                    "Error: la cilindrada debe ser un número positivo")
            cilindradaok = True
        except AttributeError as e:
            print(e)
        except ValueError:
            print("Error: la cilindrada debe ser un número")

    return {"Marca": marca, "Modelo": modelo, "Color": color, "Cilindrada": cilindrada}

"""print(diccionarioVehiculo2())"""


"""crea un diccionario con las claves marca , color , tipo , moto"""


def crear_diccionario():
    # diccionario = {marca : " " , color : " " , tipo : " " , año : " " , combustible : " "  , cilindraje : " "}
    diccionario = {}
    marcaOK = False
    while not marcaOK:
        marca = input("Introduce la marca: ").capitalize()
        if marca.isalpha():
            diccionario["marca"] = marca
            marcaOK = True
        else:
            print("La marca no pueden ser numeros")

    colorOK = False
    while not colorOK:
        color = input("Introduce el color: ")
        if color.isalpha():
            diccionario["color"] = color
            colorOK = True
        else:
            print("Color invalido introduce uno valido porfavor")

    tipoOK = False
    while not tipoOK:
        try:
            tipos = ["Deportivo" , "Electrico" ,"Hibrido" , "Mono Volumen" , "Convertible" , "SUV"]
            tipo = input("Introduce el tipo del coche: ").capitalize()
            if not tipo in tipos:
                raise ValueError("Tipo de coche invalido , escoge uno valido de estos: [Deportivo,Electrico,Hibrido,MonoVolumen,Convertible,SUV]")
            else:
                diccionario["tipo"] = tipo
                tipoOK = True
        except ValueError as e:
            print(f"ERROR: {e}")

    añoOK = False
    while not añoOK:
        try:
            año = int(input("Introduce el año del coche: "))
            if año > 2024 or año < 1880:
                raise ValueError("El año no puede ser mayor a 2024 y no puede ser menor a 1880")
            else:
                diccionario["año"] = año
                añoOK = True
        except ValueError as v:
            print(f"ERROR: {v}")

    combustibleOK = False
    while not combustibleOK:
        combustible = input("Introduce el tipo de combustible: ")
        if combustible.isalpha():
            diccionario["combustible"] = combustible
            combustibleOK = True
        else:
            print("Ingresa un tipo de combustible valido")

    cilindradaOK = False
    while not cilindradaOK:
        try:
            cilindraje = int(input("Introduce el cilindraje: "))
            if cilindraje <= 0:
                raise ValueError("La cilindradra no puede ser negativa o ser letras")
            else:
                cilindradaOK = True
                cilindrajeBIEN = (f"{cilindraje}  CC ")
                diccionario["cilindraje"] = cilindrajeBIEN
        except ValueError as v:
            print(f"ERROR: {v}")



print(crear_diccionario())

def dato_especifico(diccionario:dict , dato:str):
    pass

