#Modo-1:

def intercambiar_valores_1(a,b):
    a, b = b, a
    return a, b

#Modo-2:
def intercambiar_valores_2(a,b):
    return b, a

#Modo-3:
def intercambiar_valores_3(a,b):
    aux = a
    a = b
    b = aux
    return a, b

if __name__=="__main__":
    a = int(input("Introduce el primer número: "))
    b = int(input("Introduce el segundo número: "))
print(f"Antes de intercambiar: a = {a}, b = {b} y despues de intercambiar: {intercambiar_valores_1(a,b)}")


if __name__=="__main__":
    a = int(input("Introduce el primer número: "))
    b = int(input("Introduce el segundo número: "))
    print(f"Antes de intercambiar: a = {a}, b = {b} y despues de intercambiar: {intercambiar_valores_2(a,b)}")

if __name__=="__main__":
    a = int(input("Introduce el primer número: "))
    b = int(input("Introduce el segundo número: "))
    print(f"Antes de intercambiar: a = {a}, b = {b} y despues de intercambiar: {intercambiar_valores_3(a,b)}")
