"""Diseñar un algoritmo que lea del teclado un número entero correspondiente a una cantidad de minutos y nos
diga cuántos días, horas y minutos son. Por ejemplo: 1000 minutos, son 0 días, 16 horas y 40 minutos."""

minutos = int(input("Ingrese los minutos: "))
dias = minutos // 1440
horas = (minutos % 24 )  
minutos = minutos % 60

print(dias , horas , minutos)