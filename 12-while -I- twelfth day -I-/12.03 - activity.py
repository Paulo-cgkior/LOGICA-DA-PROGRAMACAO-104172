import os
os.system("cls")


while True:
    primeira_nota = int(input("Digite sua primeira nota: "))
    segunda_nota = int(input("Digite sua segunda nota: "))
    media = (primeira_nota + segunda_nota) / 2
    if primeira_nota < 0 or primeira_nota > 10 or segunda_nota < 0 or segunda_nota > 10:
        print("Dados incorretos")
    else:
        print (f"Nota 1: {primeira_nota}")
        print (f"Nota 2: {segunda_nota}")
        print (f"media: {media}")
        break