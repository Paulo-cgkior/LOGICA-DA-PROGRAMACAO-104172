import os
os.system("cls")

idade = int(input("Digite a idade: "))

if idade < 16:
    print("Você não está apto(a) para votar")

if idade == 17:
    print("Você está apto(a) para votar")
if idade == 16:
    print("Você está apto(a) para votar")

if idade > 17:
    print("Seu voto é obrigatorio")

elif idade >= 65:
    print("Você não é obrigado a votar")



