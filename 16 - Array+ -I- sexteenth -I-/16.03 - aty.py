import os
os.system("cls")

print("= INSERINDO 5 LIVROS NO VETOR =")

vetor_notas = []

for i in range(3):
    notas = float(input(f"DIGITE A {i+1} NOTA: "))
    vetor_notas.append(notas)

print("\n = EXIBINDO AS NOTAS = ")

for i, notas in enumerate (vetor_notas, start=1):
    print(f"{i}° : {notas}")