import os
os.system("cls")

soma = 0

for i in range(5):
    numero = int(input("Digite seus 5 numeros para soma: "))
    soma = numero + soma

print(f"Soma: {soma}")