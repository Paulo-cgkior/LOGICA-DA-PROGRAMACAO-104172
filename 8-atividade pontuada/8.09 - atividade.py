import os
os.system("cls")

renda_mensal = float(input("Digite a sua renda mensal: "))

valor_solicitado = float(input("Digite o valor solicitado: "))
limite_do_valor_do_emprestimo = renda_mensal * 10

numero_prestacoes = float(input("Digite a sua numero de prestações: "))
limite_do_valor_da_prestacao = renda_mensal / 0.30
valor_da_prestação =  valor_solicitado / numero_prestacoes

if valor_solicitado < limite_do_valor_do_emprestimo and valor_da_prestação < limite_do_valor_da_prestacao:
    print ("Empréstimo poderá ser concedido")
else:
    print("Empréstimo não poderá ser concedido")

print (f"Sua renda mensal: {renda_mensal}")
print (f"Valor solicitado: {valor_solicitado}")
print (f"Quantidade de prestações: {numero_prestacoes}")
print (f"Valor da prestação: {valor_da_prestação}")




# o valor total não deve passar de 10x a renda mensal
# as prestações devem ser no maximo 30% da renda mensal