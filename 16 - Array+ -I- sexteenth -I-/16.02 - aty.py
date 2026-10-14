import os
os.system("cls")

print("= INSERINDO 5 LIVROS NO VETOR =")

vetor_livros = []

for i in range(5):
    livros = str(input(f"DIGITE O {i+1}° LIVRO: "))
    vetor_livros.append(livros)

print("\n = EXIBINDO NOME DOS LIVROS = ")

for i, livros in enumerate (vetor_livros, start=1):
    print(f"{i}°:{livros}")