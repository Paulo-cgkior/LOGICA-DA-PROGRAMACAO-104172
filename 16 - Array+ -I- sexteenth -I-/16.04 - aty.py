import os
os.system("cls")

vetor_numero = []

for i in range(5):
    numero = float(input("Digite seu número: "))
    vetor_numero.append(numero)

print("\n = EXIBINDO AS NOTAS = ")

for i, notas in enumerate (vetor_notas, start=1):
    print(f"{i}° : {notas}")