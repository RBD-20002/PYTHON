print("<"+"-"*30+"CONJUNTOS"+"-"*30+">")

# Escribir un programa que cree dos conjuntos y encuentre la intersección y la unión de los dos conjuntos.


def conjunto_union_interseccion(conjunto1: set, conjunto2: set):
    try:
        return {f"union = {conjunto1.union(conjunto2)} , interseccion = {conjunto1.intersection(conjunto2)}"}
    except:
        print("ERROR: los conjuntos tienen que ser de tipo set")
        return None


"""print(conjunto_union_interseccion({1,2,3,4,5,6} , {7,8,9,10,5,6}))
print("-"*20)
print(conjunto_union_interseccion({1,2,3,4,5,6} , {}))
print("-"*20)
print(conjunto_union_interseccion({1,2,3,4,5,6} , [1,2,4,5]))"""

# Escribir un programa que elimine los duplicados de una lista y devuelva un conjunto.


def lista_sin_duplicados(lista: list):
    return set(lista)


"""print(lista_sin_duplicados([1,2,3,4,5,8,4,1,2,3]))"""

# Escribir un programa que determine si un conjunto dado es un subconjunto de otro conjunto dado.


def es_conjunto(conjunto1: set, conjunto2: set):
    try:
        if not isinstance(conjunto1, set) or not isinstance(conjunto2, set):
            raise TypeError("Los dos argumentos deben ser set")
        return conjunto1.issubset(conjunto2)
    except TypeError as t:
        print(f"ERROR: {t}")
        return None
    except:
        print("ERROR: fallo inesperado")
        return None


"""print(es_conjunto({1,2} , {4,1,2,5,9,6,3}))
print("-"*20)
print(es_conjunto({1,2,3,4,5} , [1,3,3,4,6,5,7]))"""

# Escribir un programa que determine la diferencia simétrica entre dos conjuntos.


def diferencia_simetrica(conjunto1: set, conjunto2: set):
    try:
        if not isinstance(conjunto1, set) or not isinstance(conjunto2, set):
            raise TypeError("Los dos argumentos deben ser set")
        return conjunto1.symmetric_difference(conjunto2)
    except TypeError as t:
        print(f"ERROR: {t}")
        return None
    except:
        print("ERROR: fallo inesperado")
        return None


"""print(diferencia_simetrica({1,2,3,4,5} , {4,5,6,7}))
print("-"*20)
print(diferencia_simetrica({1,2,3,4,5} , ["a","b","c",4,5]))"""

# Escribir un programa que determine si un conjunto dado es un conjunto vacío o no.


def conjunto_vacio(conjunto1: set):
    try:
        if not isinstance(conjunto1, set):
            raise TypeError("La funcion solo acepta conjuntos o listas")
        if len(conjunto1) == 0:
            return "El conjunto esta vacio"
        return "El conjunto no esta vacio"

    except TypeError as t:
        print(f"ERROR: {t}")
        return None
    except:
        print("ERROR: fallo inesperado")
        return None


"""print(conjunto_vacio({}))
print("-"*20)
print(conjunto_vacio({1,2,3,4,5}))
print("-"*20)
print(conjunto_vacio(["a","b","c"]))"""