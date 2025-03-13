#Modo-1:

def numero_mayor(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return print(f"El {num1} es el mayor")
    elif num2 > num1 and num2 > num3:
        return print(f"El {num2} es el mayor")
    else:
        return print(f"El {num3} es el mayor")
    
if __name__=="__main__":
    num1 = int(input("Introduce num1:"))
    num2 = int(input("Introduce num2: "))
    num3 = int(input("Introduce num3: "))
numero_mayor(num1, num2, num3)

