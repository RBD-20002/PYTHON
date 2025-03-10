"""
Escribir una función que reciba un diccionario con el horario de un alumno y
lo recorra imprimiendo los días de la semana y las asignaturas que tiene en cada uno.
"""
def imprimir_horario(horario):
    for dia,clases in horario.items():
        print(f"{dia}: {" , ".join(clases)}")
    
horario = {"lunes": {"lenguaje","fisica"}, "martes": {"biologia", "matematicas"}}
imprimir_horario(horario)