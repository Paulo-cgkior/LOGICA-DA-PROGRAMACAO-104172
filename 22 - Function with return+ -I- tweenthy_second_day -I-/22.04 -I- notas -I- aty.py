import os
os.system("cls")

soma = 0
notas = []

def funcao_media (soma):
    resultado = soma / 2
    return resultado

def funcao_apro_repro(nota):
    if nota <= 10:
        if nota >= 7:
            print("Aluno Aprovado")
        else:
            print("Aluno Reprovado")
    elif nota < 0:
        print("Primeira ou segunda nota menor que 0 ou acima de 10")
    else:
        print("Primeira ou segunda nota menor que 0 ou acima de 10")

print("= SOLICITANDO DADOS =")

for i in range(2):
    nota =+ float(input("Digite sua nota: "))
    soma += nota
    notas.append(nota)

resultado_media = funcao_media(soma)

print("\n= EXIBINDO DADOS =")
print(f"Nota = {notas}")
print(f"Soma = {soma}")
print(f"Resultado da media = {resultado_media}")
funcao_apro_repro(nota)