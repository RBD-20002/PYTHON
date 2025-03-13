"""Diseñar un algoritmo que pida una nota (valor entero) por teclado y dependiendo de su valor 
visualice la nota en letras. Por ejemplo, si nota es igual a 7 tiene que mostrar el texto Notable"""

nota = int(input("Ingrese su nota: "))
if nota >= 0 and nota <= 5:
    print("SUSPENSO")
elif nota >=6 and nota <= 7:
    print("APROBADO")
elif nota >=8 and nota <= 9:
    print("NOTABLE")
elif nota == 10:
    print("SOBRESALIENTE")
    
