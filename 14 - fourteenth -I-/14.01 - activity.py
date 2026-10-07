import os
os.system("cls")

soma = 0
contador = 0

while True:
        nota = float(input("Digite sua nota: "))
        pergunta = str(input("Deseja inserir mais uma nota? (S/N):\n")).lower()
        contador += 1
        if pergunta == "Y".lower():
            soma += nota
            media = soma / contador
            input("Digite qualquer tecla para continuar ...")
        elif pergunta == "N".lower():
            break
        else:
            print("Dados incorretos")
            break

print(f"contador: {contador}")
print(f"media: {media}")