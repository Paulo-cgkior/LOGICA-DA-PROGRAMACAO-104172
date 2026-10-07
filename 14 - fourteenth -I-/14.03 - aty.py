import os
os.system("cls")

soma = 0
contador = 0

while True:
        numero = int(input("Digite seu numero: "))
        if numero > 0:
            contador += 1
            soma += numero
        else:
            media = soma / contador
            print (f"Media: {media}")
            break