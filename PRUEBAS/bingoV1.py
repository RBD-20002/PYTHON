
import random

# Genera un cartón de bingo con 5 columnas (B, I, N, G, O) y 5 filas.
def generar_carton():
    carton = {'B': [], 'I': [], 'N': [], 'G': [], 'O': []}
    for i, letra in enumerate(carton):
        inicio = i * 15 + 1
        carton[letra] = random.sample(range(inicio, inicio + 15), 5)
    
    # Coloca un espacio libre en el centro del cartón
    carton['N'][2] = 'X'
    return carton

# Imprime el cartón en formato de tabla
def imprimir_carton(carton):
    print(" B   I   N   G   O ")
    for fila in range(5):
        for letra in carton:
            valor = carton[letra][fila]
            print(f"{valor:>2} ", end=" ")
        print()  # Nueva línea al final de cada fila

# Extrae números aleatorios entre 1 y 75 sin repetir
def extraer_numeros():
    numeros = list(range(1, 99))
    random.shuffle(numeros)
    return numeros

# Verifica si un cartón es ganador (completa una línea o columna)
def verificar_ganador(carton, marcados):
    # Verificar filas y columnas
    for i in range(5):
        if all(carton[letra][i] in marcados or carton[letra][i] == 'X' for letra in carton):
            return True
        if all(carton[letra][i] in marcados or carton[letra][i] == 'X' for letra in carton):
            return True
    # Verificar diagonales
    if all(carton[letra][i] in marcados or carton[letra][i] == 'X' for i, letra in enumerate(carton)):
        return True
    if all(carton[letra][4 - i] in marcados or carton[letra][4 - i] == 'X' for i, letra in enumerate(carton)):
        return True
    return False

# Jugar al bingo
def jugar_bingo():
    carton = generar_carton()
    imprimir_carton(carton)
    numeros = extraer_numeros()
    marcados = set()

    print("\nExtrayendo números...\n")
    for numero in numeros:
        print(f"Número extraído: {numero}")
        marcados.add(numero)
        if verificar_ganador(carton, marcados):
            print("¡Bingo! Has completado el cartón.")
            break

# Ejecutar el juego
jugar_bingo()



print("__________________")
import random


def inicio() -> bool:
  while True:
    inicio = input("Te gustaría jugar al Bingo? Y/N: ").upper()
    if inicio == "Y":
      input("Elige un número del 1 al 100 para seleccionar tu cartón: ")
      return True
    elif inicio == "N":
      print("Que pena, es muy divertido.")
      return False
    else:
      print("No te entendí. Por favor, responde con 'Y' o 'N'.")
    
def generacion_de_carton() -> list:
  matriz= []
  while len(matriz) < 25:
    numero_aleatorio = random.randint(0,100) 
    if numero_aleatorio not in matriz:
      matriz.append(numero_aleatorio)
  carton = [matriz[i:i+5] for i in range(0,25,5)]    #Forma el carton en matriz (ChatGPT)
  return carton

carton = generacion_de_carton()

def imprimir_carton(carton: list):
  print("Genial! Este es tu carton de Bingo: ")
  for fila in carton:
    print(" ".join(f"{num:3}" for num in fila))  #Matriz impresa en forma de "matriz" (ChatGPT)
  print("Bien! Si todo el mundo tiene su cartón, vamos a comenzar!")

def sacar_numeros_bingo() -> int:
  numeros_retirados=[]
  numero = None
  while True:
    numero = random.randint(0,100)
    numeros_retirados.append(numero)
    if numero not in numeros_retirados:
       print(f"Número",{numero},"alguien lo tiene?")


#def verificar_carton() -> bool:
 

if __name__ == "_main_":
   inicio()
   generacion_de_carton()
   imprimir_carton(carton)
   sacar_numeros_bingo()