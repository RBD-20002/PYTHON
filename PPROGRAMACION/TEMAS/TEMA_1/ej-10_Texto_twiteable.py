"""Implementar un programa que verifique si un texto es 
"Twiteable" (tiene 280 caracteres o menos) o no."""

twit = input("Ingrese twit: ")
if len(twit) <= 280:
    print("El twit es Twiteable")
else:
    print("El twit no es Twiteable")