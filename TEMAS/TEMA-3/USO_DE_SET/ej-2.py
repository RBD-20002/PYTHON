"""
Escribir una función que reciba dos conjuntos y devuelva un conjunto 
con los elementos que están en el primer conjunto pero no en el segundo.
"""
def diferencias(conjunto:set , conjunto2:set):
    try:
        if not isinstance(conjunto,set) or not isinstance(conjunto2,set):
            raise TypeError("Ambos argumentos deben ser conjuntos")
        return conjunto.difference(conjunto2)
    
    except TypeError:
        print("ERROR: los argumentos de la funcion deben ser conjuntos")
        return None
    except:
        print("ERROR: fallo inesperado")
        return None

print(diferencias( {1,2,3,4,5,6} , {4,5,6,7,8,9}))
print("-"*20)
print(diferencias( {1,2,3,4,5} , []))