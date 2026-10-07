import os
os.system("cls")

contador = 0
pares = 0
impares = 0
soma = 0
somap = 0
somai = 1

while True:
    numero = int(input("Digite seu numero: "))
    if numero > 0:
        contador += 1
        soma += numero
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    else:
            media = soma / contador
            print(f"par: {pares}")
            print(f"impar: {impares}")
            break

