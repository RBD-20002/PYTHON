print("------------------------------INTERCAMBIAR")
def intercambiar():
    a = int(input("Valor de A: "))
    b = int(input("Valor de B: "))
    print(f"Antes de cambiar A vale {a} y B vale {b}")
    a , b = b , a
    print(f"Despues de cambiar A vale {a} y B vale {b}")
intercambiar()

print("------------------------------NUMERO MAYOR")
def numero_mayor():
    a = int(input("Valor de A: "))
    b = int(input("Valor de B: "))
    c = int(input("Valor de C: "))
    if a > b and a > c:
        return print(f"El numero mayor es {a}")
    elif b > a and b > c:
        return print(f"El numero mayor es {b}")
    return print(f"El numero mayor es {c}")
numero_mayor()

print("------------------------------NUMERO EULER")
def factorial(numero):
    if numero == 0:
        return 1
    return numero * factorial(numero - 1)
def numero_euler():
    numero = int(input("Numero: "))
    suma = 0
    for i in range(numero):
        suma += 1 / factorial(i)
    return print(suma)
numero_euler()

print("------------------------------CONTADOR CARACTER")
def contador_caracter():
    caracter = input("Caracter: ")
    texto = input("Texto: ")
    for letra in texto:
        if letra.lower() == caracter.lower():
            return print(f"El caracter '{caracter}' se repite {texto.count(letra)} veces")
contador_caracter()

print("------------------------------INVERTIR NUMERO")
def invertir_numero():
    numero = int(input("Numero: "))
    guardar = numero
    while numero < 0:
        print("El numero debe ser positivo")
        numero = int(input("Numero: "))
    invertir = 0
    while numero > 0:
        digito = numero % 10
        numero //= 10
        invertir = invertir * 10 + digito
    return print(f"El numero {guardar} al invertirlo es {invertir}")
invertir_numero()

print("------------------------------NUMEROS AMIGOS")
def suma_divisores(numero):
    suma = 0 
    for i in range(1 , numero //2 + 1):
        if numero % i == 0:
            suma += i
    return suma 
def numero_amigos():
    num1 = int(input("Num1: "))
    num2 = int(input("Num2: "))
    if suma_divisores(num1) == num2 and suma_divisores(num2) == num1:
        return print(f"Los numeros {num1} y {num2} son amigos")
    return print(f"Los numeros {num1} y {num2} no son amigos")
numero_amigos() 
    
print("------------------------------NUMERO PERFECTO")
def numero_perfecto():
    numero = int(input("Numero: "))
    while numero < 0:
        print("El numero no puede ser negativo")
        numero = int(input("Numero: "))
    suma = 0
    for i in range(1 , numero//2 + 1):
        if numero % i == 0:
            suma += i
    if suma == numero:
        return print(f"El numero {numero} es perfecto")
    return print(f"El numero {numero} no es perfecto")
numero_perfecto()

print("------------------------------REGISTRAR Y VALIDAR USUARIO")
def registrar():
    global usuario , password
    usuario = input("Usuario: ")
    password = input("Contraseña: ")
    repite_password = input("Repite la contraseña: ")
    while password != repite_password:
        print("Las contraseñas no coinciden")
        password = input("Contraseña: ")
        repite_password = input("Repite la contraseña: ")
    print("Usuario registrado con éxito")
def login(contador = 3):
    contador_intentos = 0
    while contador_intentos < contador:
        usuario_login = input("Usuario: ")
        password_login = input("Contraseña: ")
        if password_login != password:
            print("Contraseña incorrecta")
            contador_intentos += 1
            if contador_intentos == contador:
                print("Has superado el número de intentos permitidos")
        if password_login == password and usuario_login == usuario:
            print("Login exitoso")
            break
registrar()
login()
    
print("------------------------------CALCULADORA")
def menu():
    print("|   CALCULADORA   |")
    print("|suma             |")
    print("|resta            |")
    print("|multiplicacion   |")
    print("|division         |")
    print("|potencia         |")
    print("|division entera  |")
    print("|modulo           |")
    print("|raiz             |")
    print("|salir            |")
def suma(a,b):
    return a + b
def resta(a,b):
    return a - b
def multiplicacion(a,b):
    return a * b
def division(a,b):
    if b == 0:
        return print("No se puede dividir entre 0")
    return a / b
def division_entera(a,b):
    if b == 0:
        return print("No se puede dividir entre 0")
    return a // b
def potencia(a,b):
    return a ** b
def modulo(a,b):
    if b == 0:
        return print("No se puede dividir entre 0")
    return a % b
def raiz(a):
    if a < 0:
        print("No se puede calcular la raiz cuadrada de un numero negativo")
    return a ** 0.5
def lista_opcion():
    return ["suma", "resta", "multiplicacion", "division", "potencia", "division_entera", "modulo", "raiz", "salir"]
def validar_opcion(a,b,opcion):
    match opcion:
        case "suma":
            return suma(a,b)
        case "resta":
            return resta(a,b)
        case "multiplicacion":
            return multiplicacion(a,b)
        case "division":
            return division(a,b)
        case "potencia":
            return potencia(a,b)
        case "division_entera":
            return division_entera(a,b)
        case "modulo":
            return modulo(a,b)
        case "raiz":
            return raiz(a)
        case "salir":
            return None
        case "":
            return print("Opcion no valida")
def calculadora():
    menu()
    while True:
        opcion = input("Opcion: ").lower()
        if opcion == "raiz":
            a = float(input("Numero: "))
            print(f"La raiz cuadrada de {a} es {raiz(a)}")
        elif opcion in lista_opcion():
            a = float(input("Numero 1: "))
            b = float(input("Numero 2: "))
            print(f"El resultado es {validar_opcion(a,b,opcion)}")
        elif opcion == "salir":
            print("Adiós")
            break
calculadora()

print("------------------------------CALCULAR AREA Y PERIMETRO")
def circunferencia():
    radio = float(input("Radio: "))
    area = 3.14 * (radio**2)
    perimetro = 2 * 3.14 * radio
    print(f"El area es {area} y el perimetro es {perimetro}")
def rectangulo():
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    area = base * altura
    perimetro = 2 * (base + altura)
    print(f"El area es {area} y el perimetro es {perimetro}")
def cuadrado():
    lado = float(input("Lado: "))
    area = lado ** 2
    perimetro = 4 * lado
    print(f"El area es {area} y el perimetro es {perimetro}")
def triangulo_equilatero():
    lado = float(input("Lado: "))
    area = ((3)*0.5 / 4) * (lado ** 2)
    perimetro = 3 * lado 
    print(f"El area es {area} y el perimetro es {perimetro}")
def menu():
    print("|    CALCULADORAS    |")
    print("|circunferencia      |")
    print("|rectangulo          |")
    print("|cuadrado            |")
    print("|triangulo equilatero|")
    print("|salir               |")
def validar_ocpion(opcion):
    match opcion:
        case "circunferencia":
            circunferencia()
        case "rectangulo":
            rectangulo()
        case "cuadrado":
            cuadrado()
        case "triangulo equilatero":
            triangulo_equilatero()
        case "salir":
            return None
        case "":
            print("Opcion no valida")
def lista_opcion():
    return ["circunferencia", "rectangulo", "cuadrado", "triangulo equilatero", "salir"]
def calculo():
    menu()
    while True:
        opcion = input("Opcion: ")
        if opcion in lista_opcion():
            validar_ocpion(opcion)
        if opcion == "salir":
            print("Adiós")
            break
calculo()

print("------------------------------POSICION NUMERO MAXIMO Y NUMERO MAYOR")
def crear_lista():
    numero = int(input("Pedido: "))
    lista = []
    for i in range(numero):
        lista.append(int(input(f"Introduce numero {i+1}: ")))
    return lista
def PosicionNumeroMayor():
    lista = crear_lista()
    numero_maximo = max(lista)
    posicion = lista.index(numero_maximo)
    print(f"El numero maximo es {numero_maximo} y se encuentra en la posicion {posicion+1}")
PosicionNumeroMayor()

print("------------------------------INVERTIR LISTA")
def invertir_lista():
    lista = crear_lista()
    nueva_lista = []
    for i in range(len(lista)-1, -1, -1):
        nueva_lista.append(lista[i])
    print(f"La lista original es {lista} y la invertida es {nueva_lista}")
invertir_lista()

print("------------------------------PROBLERMAS VARIADOS LISTAS")
def crear_lista():
    nº_pedidos = int(input("Numeros: "))
    lista = []
    for i in range(nº_pedidos):
        numero = int(input("Numero: "))
        lista.append(numero)
    return lista
crear_lista()
def suma_lista():
    lista = crear_lista()
    suma = 0
    for i in lista:
        suma += i
    return print(f"La suma de los elementos de la lista es {suma}")
suma_lista()
def numero_mayor_lista():
    lista = crear_lista()
    mayor = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    return print(f"El numero mayor es {mayor}")
numero_mayor_lista()
def media_lista():
    lista = crear_lista()
    suma = 0
    for i in lista:
        suma += i 
    media = suma / len(lista)
    return print(f"La media de los elementos de la lista es {media}")
media_lista()
def mediana_lista():
    lista = crear_lista()
    lista.sort()
    if len(lista) % 2 == 0:
        mediana = (lista(len(lista)// 2)) + (lista(len(lista)//2 - 1)) / 2
        return print(f"La mediana de los elementos de la lista es {mediana}")
    else:
        mediana = lista[len(lista)//2]
        return print(f"La mediana de los elementos de la lista es {mediana}")
mediana_lista()
def varianza_lista():
    lista = crear_lista()
    media = (sum(lista)/len(lista))
    suma_cuadrados = 0
    for i in lista:
        suma_cuadrados += (i - media) ** 2
    varianza = suma_cuadrados / len(lista)
    return print(f"La varianza de los elementos de la lista es {varianza}")
varianza_lista()
def desviacion_tipica():
    lista = crear_lista()
    media = (sum(lista) / len(lista))
    suma_cuadrados = 0
    for i in lista:
        suma_cuadrados += (i - media) ** 2
    varianza = suma_cuadrados / len(lista)
    desviacion_tipica = varianza ** 0.5
    return print(f"La desviacion tipica de los elementos de la lista es {desviacion_tipica}")
desviacion_tipica()
def simetrica_lista():
    lista = crear_lista()
    lista_invertida = lista[::-1]
    if lista == lista_invertida:
        return print("La lista es simetrica")
    else:
        return print("La lista no es simetrica")
simetrica_lista()
def esPrimo(numero: int) -> bool:
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True
def primosLista(lista: list) -> list:
    primos = []
    for numero in lista:
        if esPrimo(numero):
            primos.append(numero)
    return primos
def esCapicua(numero: int):
    return str(numero) == str(numero)[::-1]
def capicuasLista(lista: list) -> list:
    capicuas = []
    for numero in lista:
        if esCapicua(numero):
            capicuas.append(numero)
    return capicuas
