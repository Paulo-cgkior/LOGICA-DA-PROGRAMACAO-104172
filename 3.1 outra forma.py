import os
os.system("cls")

idade = int(input("Digite a idade: "))

if idade < 16:
    print("Você não está apto(a) para votar")

elif idade < 18:
    print("Você está apto(a) para votar")

elif idade <= 65:
    print("Voto obrigatorio")

else:
    print("Não obrigado a votar")