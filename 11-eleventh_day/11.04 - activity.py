import os
os.system("cls")

print("ACUMULANDO VALORES EM UMA VARIÁVEL")
soma = 0

print(f"Valor da variável soma: {soma}")
numero = int(input("\nDigite um número para somar: "))

for i in range(3):
    soma = soma + numero
    print(f"Valor Temporario da variável soma: {soma}")

print(f"Valor Final da variável soma: {soma}")