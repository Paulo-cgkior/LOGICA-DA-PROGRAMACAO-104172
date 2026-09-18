import os
os.system("cls")

quantidade_de_macas = float(input("Digite a quantidade de maças: "))

if quantidade_de_macas >= 12:
    macas = 1.00
else:
    macas = 1.30

print(f"Valor a pagar: {quantidade_de_macas * macas:.3f}")
