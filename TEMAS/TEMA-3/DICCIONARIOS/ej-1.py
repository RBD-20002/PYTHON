"""
Escribir una función que reciba un diccionario con las asignaturas y 
las notas de un alumno y devuelva otro diccionario con las asignaturas 
en mayúsculas y las calificaciones correspondientes a las notas aprobadas.
"""
def diccionario(asignatura: dict) -> dict:
    try:
        if not isinstance(asignatura, dict):
            raise ValueError("Error: El argumento debe de ser un diccionario")
        if not asignatura:
            raise KeyError("Error: El diccionario no puede estar vacío")
        resultado = {}
        for asignatura, nota in asignatura.items():
            asignatura = asignatura.strip().lower()
            if nota < 0 or nota > 10:
                raise ValueError(f"Error: Las notas para {asignatura} deben de ser entre 0 y 10")
            if not isinstance(nota, (int, float)):
                raise TypeError(f"Error: La nota para {asignatura} debe ser un número.")
            if nota < 5:
                resultado[asignatura.capitalize()] = ("Suspenso", nota)
            elif 5 <= nota < 6:
                resultado[asignatura.capitalize()] = ("Suficiente", nota)
            elif nota >= 6 and nota < 8:
                resultado[asignatura.capitalize()] = ("Bien", nota)
            elif nota >= 8 and nota < 9:
                resultado[asignatura.capitalize()] = ("Notable", nota)
            elif nota >= 9 and nota < 10:
                resultado[asignatura.capitalize()] = ("Sobresaliente", nota)
            elif nota == 10:
                resultado[asignatura.capitalize()] = ("Matrícula de honor", nota)
        return resultado
    except KeyError as e:
        print(e)
        return {}
    except ValueError as e:
        print(e)
        return {}
    except TypeError as e:
        print(e)
        return {}
    except:
        print("Error inesperado")
        return {}
   
print(diccionario({
    "Matemáticas": 8.5,
    "Lengua": 9.2,
    "Historia": 7.8,
    "Ciencias": 8.0,
    "Inglés": 9.5,
    "Física": 6.7,
    "Química": 8.3
}))
print(diccionario({}))
print(diccionario([]))
print(diccionario({
    "Matemáticas": 18.5,
    "Lengua": 9.2,
    "Historia": 7.8,
    "Ciencias": 8.0,
    "Inglés": 9.5,
    "Física": 6.7,
    "Química": 8.3
}))