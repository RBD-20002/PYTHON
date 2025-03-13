"""
Escribir una función que reciba un diccionario y una clave y devuelva el valor asociado a la clave.
Si la clave no existe debe devolver un mensaje de error.
"""

def obtener_valor_diccionario(diccionario: dict, clave: str) -> str:
    try:
        return diccionario[clave]
    except KeyError:
        return "La clave no existe en el diccionario."

# Pruebas

diccionario = {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 30,
    "direccion": "Gar"
}

print(obtener_valor_diccionario(diccionario, "nombre"))  # Devuelve: Juan

print(obtener_valor_diccionario(diccionario, "telefono"))  # Devuelve: La clave no existe en el diccionario.

print(obtener_valor_diccionario({}, "clave_inexistente"))  # Devuelve: La clave no existe en el diccionario.

