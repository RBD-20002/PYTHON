
print("------------------------------AÑO BISIESTO MODO 1")


def es_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False

año = int(input("Introduce un año: "))
if es_bisiesto(año):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")

print("------------------------------AÑO BISIESTO MODO 2")


def is_year_leap(year):
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        return False
    else:
        return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")


print("------------------------------CONTEO DE DIAS")


def is_year_leap(year):
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        return False
    else:
        return True

def days_in_month(year, month):
    if month < 1 or month > 12:
        return None
    if month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")


print("------------------------------ULTIMO DIA DEL MES")


def last_day_of_month(year, month):
    return days_in_month(year, month)


# Pruebas
test_years = [1900, 2000, 2023, 2024]
test_months = [2, 2, 6, 11]
expected_results = [28, 29, 30, 30]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    result = last_day_of_month(yr, mo)
    print(f"{yr}-{mo} -> Último día: {result} ->", "OK" if result ==
          expected_results[i] else f"Fallido (Esperado: {expected_results[i]})")


print("------------------------------NUMERO PRIMO")


def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


# Pruebas
test_numeros = [2, 4, 7, 9, 13, 16]
test_resultados = [True, False, True, False, True, False]

for i in range(len(test_numeros)):
    resultado = es_primo(test_numeros[i])
    print(f"{test_numeros[i]} -> {'Primo' if resultado else 'No primo'} ->",
          "OK" if resultado == test_resultados[i] else "Fallido")


print("------------------------------NUMERO PERFECTO")


def es_numero_perfecto(numero):
    suma_divisores = sum(i for i in range(
        1, numero // 2 + 1) if numero % i == 0)
    return suma_divisores == numero


# Pruebas
test_numeros = [6, 28, 12, 496, 8128]
test_resultados = [True, True, False, True, True]

for i in range(len(test_numeros)):
    resultado = es_numero_perfecto(test_numeros[i])
    print(f"{test_numeros[i]} -> {'Perfecto' if resultado else 'No perfecto'} ->",
          "OK" if resultado == test_resultados[i] else "Fallido")


print("------------------------------CAMBIO DE TEMPERATURA")


def convertir_temperatura(valor, origen, destino):
    if origen == 'C':
        if destino == 'F':
            return valor * 9/5 + 32
        elif destino == 'K':
            return valor + 273.15
    elif origen == 'F':
        if destino == 'C':
            return (valor - 32) * 5/9
        elif destino == 'K':
            return (valor - 32) * 5/9 + 273.15
    elif origen == 'K':
        if destino == 'C':
            return valor - 273.15
        elif destino == 'F':
            return (valor - 273.15) * 9/5 + 32
    return None

# Pruebas
test_datos = [
    (0, 'C', 'F', 32),
    (100, 'C', 'K', 373.15),
    (212, 'F', 'C', 100),
    (273.15, 'K', 'C', 0),
]
for valor, origen, destino, esperado in test_datos:
    resultado = convertir_temperatura(valor, origen, destino)
    print(f"{valor}°{origen} -> {destino}: {resultado} ->", "OK" if round(resultado, 2)
          == round(esperado, 2) else f"Fallido (Esperado: {esperado})")