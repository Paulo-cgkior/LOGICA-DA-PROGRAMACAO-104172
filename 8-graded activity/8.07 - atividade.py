import os
os.system("cls")

nome = str(input("Digite o nome: "))
quantidade = str(input("Digite a quantidade: "))
preco_unitario = str(input("Digite o preço unitário: "))

valor_final = quantidade * preco_unitario


if quantidade <= 5:
    print (f"Valor a pagar: {valor_final / 0.02}")
elif quantidade > 5 and quantidade <= 10:
    print (f"Valor a pagar: {valor_final / 0.03}")
elif quantidade > 10:
    print (f"Valor a pagar: {valor_final / 0.05}")