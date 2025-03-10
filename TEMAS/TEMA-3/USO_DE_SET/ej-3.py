"""
Escribir una función que reciba dos conjuntos y devuelva un conjunto 
con los elementos que están en alguno de los dos conjuntos pero no en los dos.
"""
def diferentes(conjunto1:set , conjunto2:set):
    try:
        return conjunto1.symmetric_difference(conjunto2)
    
    except TypeError:
        print("ERROR: Los conjuntos deben ser de tipo set")
        return None
    except:
        print("ERROR: fallo inesperado")
        return None    
print(diferentes({1,2,3,4} , {7,8,4,5,9,1}))