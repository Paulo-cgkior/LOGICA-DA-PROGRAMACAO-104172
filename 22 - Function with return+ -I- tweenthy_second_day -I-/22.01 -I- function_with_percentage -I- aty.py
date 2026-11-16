import os
os.system("cls")

def inflacionar_reduzir (preco):
    dez_porcento = preco * 0.10
    vinte_porcento = preco * 0.20
    if preco < 100:
        resultado = preco + dez_porcento
    else:
        resultado = preco + vinte_porcento
    return resultado

print("= SOLICITANDO DADOS =")
preco = float(input("\nDigite o preço do produto= "))

resultado = inflacionar_reduzir(preco)

print("\n= EXIBINDO DADOS =")
print(f"\nPreço escolhido: {preco}")
print(f"Preço com inflação: {resultado}")