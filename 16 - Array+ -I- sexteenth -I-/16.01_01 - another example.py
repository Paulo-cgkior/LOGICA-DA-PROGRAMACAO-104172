import os
os.system("cls")

print("= INSERINDO NÚMEROS NO VETOR =")
vetor_numeros = []

for i in range(3):
    numero = int(input("Digite um número: "))
    vetor_numeros.append(numero)

print("\n= EXIBINDO NÚMEROS DO VETOR =")
print(f"Primeira posição do vetor: {vetor_numeros[0]}")

# SUA VEZ, MOSTRE A ÚLTIMA POSIÇÃO DO VETOR.

print(f"ultima posição do vetor: {vetor_numeros[2]}")