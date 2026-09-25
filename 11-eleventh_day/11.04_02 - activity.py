import os
os.system("cls")

print("\nACUMULANDO VALORES EM UMA VARIÁVEL")
soma = 0

print(f"Valor INICIAL da variável soma: {soma}")

for i in range(3):
    soma += int(input("\nDigite um número para somar: "))

print(f"Valor Final da variável soma: {soma}")