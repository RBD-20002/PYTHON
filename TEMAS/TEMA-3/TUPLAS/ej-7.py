"""
Escribir una función que reciba una tupla de números y devuelva su media y su varianza.
"""
def media_varianza(tupla:tuple):
    try:
        if not isinstance(tupla, tuple):
            raise TypeError("La funcion recibe solo tuplas")
        media = sum(tupla)/len(tupla)
        varianza = sum((x - media)**2 for x in tupla)/len(tupla)
        return [varianza , media]
    
    except TypeError as t:
        print(f"ERROR: {t}")
        return None
    except:
        print("ERROR: fallo inesperado")

print(media_varianza((1, 2, 3, 4, 5)))  
print("-------------------------------------")
print(media_varianza((1,"a",2,"b",3,"c",4,"d",5)))
print("-------------------------------------")
print(media_varianza([1,2,"a","b",3,4]))