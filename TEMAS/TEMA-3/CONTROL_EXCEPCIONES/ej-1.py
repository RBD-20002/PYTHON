"""
Escribir una función que reciba dos números y devuelva su división.
Si el segundo número es cero debe devolver un mensaje de error.
"""

def division(a: int = None, b: int = None):
    try:
        if a is None or b is None:
            raise TypeError("ERROR: deben haber 2 argumentos para que funcione")
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("ERROR: los argumentos deben ser enteros")
        return a / b
    
    except TypeError as t:
       print(f"ERROR: {t}")
       return None
    except ZeroDivisionError:
        print("ERROR: no se puede dividir entre 0")
        return None
    except Exception:
        print("ERROR: fallo inesperado")
        return None
        
        
# Ejemplos de uso
print(division(10,5))
print("-------------------------------")
print(division (10,"5"))
print("-------------------------------")
print(division(10))
print("-------------------------------")
print(division("10","5"))
print("-------------------------------")
print(division(10,0))