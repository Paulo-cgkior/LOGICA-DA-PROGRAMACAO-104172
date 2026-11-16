import os
os.system("cls")

vetor_nota = []
soma = 0

def funcao_media(media):
    media = soma / 3
    return media

print("= SOLICITANDO DADOS =")
for i in range(3):
    nota = float(input(f"Digite sua {i+1} nota: "))
    soma += nota
    vetor_nota.append(nota)

media = funcao_media(nota)

print("= EXIBINDO DADOS =")
print(f"Notas escolhidas: {vetor_nota}")
print(f"media: {media}")