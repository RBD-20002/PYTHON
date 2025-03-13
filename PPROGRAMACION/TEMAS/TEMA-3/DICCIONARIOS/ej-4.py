"""
Escribir una función que reciba un diccionario con las asignaturas y 
las notas de un alumno y devuelva la media de las notas.
"""
def media_alumno(alumnos):
    medias = {}
    for alumno , notas in alumnos.items():
        total_notas = 0
        for materia , nota in notas.items():
            total_notas += nota
        media = total_notas / len(notas)
        medias[alumno] = media
    return medias

alumnos = {"Ricardo": {"fisica": 8 , "matematicas": 5 , "lenguaje": 10 , "computacion": 9} , 
                "Jacqueline": {"fisica": 10 , "matematicas": 6 , "lenguaje": 9 , "computacion": 5},
                "Jac": {"fisica": 8 , "matematicas": 5 , "lenguaje": 10 , "computacion": 9}}

print(media_alumno(alumnos))


