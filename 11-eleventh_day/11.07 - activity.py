import os
os.system("cls")

soma = 0

for i in range(3):
    soma += int(input("Digite as notas: "))
media = soma / 3

if media < 4:
    print(f"Nota: {media} Aluno Reprovado ")
elif media < 7:
    print(f"Nota: {media} Aluno em recuperação ")
else:
    print(f"Nota: {media} Aluno Aprovado ")