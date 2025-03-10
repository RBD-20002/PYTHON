def invertir_numero(numero):
    if numero < 0: 
        return -1
    toret = 0
    while numero > 0:
        toret = toret * 10 + numero % 10
        numero = numero // 10
    return toret 

print(invertir_numero(5963))

def invertir_rebanada(numero2):
    if numero2 < 0:
        print("El numero debe ser positivo")
        return -1
    else:
        return (str(numero2)[::-1])

if __name__=="__main__":
    numero2 = int(input("introduce numero: "))
print(invertir_rebanada(numero2))