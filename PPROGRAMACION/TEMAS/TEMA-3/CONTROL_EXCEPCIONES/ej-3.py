"""
Escribir una función que reciba una cadena y un número n y devuelva la cadena repetida n veces. 
Si el número es negativo debe devolver un mensaje de error.
"""


def repetirCadena(cadena: str =None , repetir: int =None):
    try:
        if repetir is None or cadena is None:
            raise TypeError("Debes ingresar ambos argumentos")
        if not isinstance(repetir, int):
            raise TypeError("El segundo argumento solo puede ser enteros")
        return cadena * repetir
    
    except TypeError as t:
        print(f"ERROR: {t}")
        return None
    except Exception:
        print("ERROR: fallo desconocido")
        return None

# Pruebas
print(repetirCadena("Hola ", 3))
print("-------------------------------")
print(repetirCadena("hola", "3"))
print("-------------------------------")
print(repetirCadena(3))
print("-------------------------------")
print(repetirCadena("hola"))
