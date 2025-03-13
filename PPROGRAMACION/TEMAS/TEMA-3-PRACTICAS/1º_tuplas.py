print("<"+"-"*30+"TUPLAS"+"-"*30+">")

# Escribir un programa que reciba una tupla y luego imprima la suma de todos los números pares en la tupla.

def suma_tupla_v1(tupla: tuple):
    try:
        if not isinstance(tupla, tuple):
            raise TypeError("La funcion solo acepta tuplas")
        if not all(isinstance(elemento, int) for elemento in tupla):
            raise TypeError("No hay números pares en la tupla")
        return sum(i for i in tupla if i % 2 == 0)

    except TypeError as t:
        print(f"ERROR: {t}")
        return ()
    except ValueError as v:
        print(f"ERROR: {v}")
    except:
        print("ERROR: fallo inesperado")
        return ()


"""print("-"*100)
print(suma_tupla_v1((1,2,3,4,5,6,7,8)))
print("-"*20)
print(suma_tupla_v1([1,2,3,4,5,6,7,8]))
print("-"*20)
print(suma_tupla_v1(123456))
print("-"*20)
print(suma_tupla_v1(()))
print("-"*20)
print(suma_tupla_v1(("a","b","c","d")))
print("-"*100)"""


def suma_tupla_v2(tupla: tuple):
    try:
        if not isinstance(tupla, tuple):
            raise TypeError("la funcion solo acepta tuplas")
        if not all(isinstance(elemento, int) for elemento in tupla):
            raise TypeError("No hay números pares en la tupla")
        suma = 0
        for elemento in tupla:
            if elemento % 2 == 0:
                suma += elemento
        return suma

    except TypeError as t:
        print(f"ERROR: {t}")
        return None
    except:
        print("ERROR: fallo inesperado")
        return None


"""print("-"*100)
print(suma_tupla_v2((1,2,3,4,5,6,7,8)))
print("-"*20)
print(suma_tupla_v2([1,2,3,4,5,6,7,8]))
print("-"*20)
print(suma_tupla_v2(123456))
print("-"*20)
print(suma_tupla_v2(()))
print("-"*20)
print(suma_tupla_v2(("a","b","c","d")))
print("-"*100)"""

# Escribir un programa que reciba dos tuplas como entrada y devuelva una
# nueva tupla que contenga los elementos que aparecen en ambas tuplas.


def nueva_tupla(tupla1: tuple, tupla2: tuple):
    try:
        if not isinstance(tupla1, tuple) or not isinstance(tupla2, tuple):
            raise TypeError("la funcion solo acepta tuplas")
        return tuple(set(tupla1).intersection(tupla2))

    except TypeError as t:
        print(f"ERROR: {t}")
    except:
        print("ERROR: fallo inesperado")


"""print(nueva_tupla((1,2,3,4,5,6) , (5,4,6,7,8,9,10)))
print("-"*20)
print(nueva_tupla((1,2,3,4,5,6,) , [1,2,3,4,5,6]))
print("-"*20)
print(nueva_tupla((1,2,"2") , (1,"1",2)))
print(nueva_tupla(() , ()))"""

# Escribir un programa que reciba una tupla como entrada y devuelva una nueva tupla con los elementos ordenados en orden ascendente.


def tupla_ordenada(tupla: tuple):
    try:
        if not all(isinstance(elemento, int) for elemento in tupla) and not all(isinstance(elemento, str) for elemento in tupla):
            raise TypeError(
                "los argumentos de la funcion deben ser del mismo tipo")
        return tuple(sorted(list(tupla)))

    except TypeError as t:
        print(f"ERROR: {t}")
        return ()
    except:
        print("ERROR: fallo inesperado")
        retun()


"""print(tupla_ordenada((8,2,47,6,9,2,51)))
print("-"*20)
print(tupla_ordenada(("z","s","a","d",1,2,3)))
print("-"*20)
print(tupla_ordenada(("z","f","a","t","o")))
print("-"*20)
print(tupla_ordenada((2,345,543,86,1)))
print("-"*20)
print(tupla_ordenada([]))"""

# Escribir un programa que reciba una tupla como entrada y determine la posicion del elemento que se pasa como argumento.


def verificar(tupla: tuple, valor):
    try:
        return ((list(tupla)).index(valor))

    except ValueError:
        print("ERROR: el valor es invalido para esta funcion")
    except:
        print("ERROR: fallo inesperado")
        return None


"""print(verificar((1,2,3,4,5,6,7) , 5)) 
print("-"*20)
print(verificar((1,2,3,4,5) , (1,2,3,4)))
print("-"*20)
print(verificar((1,2,3,4,5) , 6))
print("-" *20)
print(verificar(("a","b","c",1) , 5  ))
print("-"*20)
print(verificar(("a","b","c","d") , "a"))"""

# Escribir un programa que reciba una tupla como entrada y cree una nueva tupla que contenga solo los elementos impares.


def tupla_impares(tupla: tuple):
    try:
        return tuple(elemento for elemento in tupla if elemento % 2 != 0)

    except TypeError:
        print("ERROR: la tupla tiene que contener numeros enteros")
        return None
    except:
        print("ERROR: fallo inesperado")
        return None


"""print(tupla_impares((1,2,3,4,5,6,7,8,9,11)))
print("-"*20)
print(tupla_impares((1,2,3,4,"d","f")))"""
