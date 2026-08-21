import os

# Limpa o terminal 
os.system("cls")

print("= SOLICITANDO OS DADOS =")
valor = float(input("Digite o valor: "))

#CALCULANDO.
#Descontando 10%
desconto = valor * 0.10
valor_com_desconto = valor - desconto

print("= EXIBINDO DADOS =")
print("Valor com desconto de 19% ", valor_com_desconto)
