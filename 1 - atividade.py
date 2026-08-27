import os 
 #Limpo o terminal
os.system("cls")
    
# Entrada.
print("= SOLICITANDO DADOS =")
primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

#Processamento.
soma = primeiro_numero + segundo_numero
subtracao = primeiro_numero - segundo_numero
multiplicacao = primeiro_numero * segundo_numero
divisao = primeiro_numero / segundo_numero

# Saida.
print("\n = EXIBINDO DADOS =")
print("soma: ", soma)
print("subtracao: ", subtracao)
print("multiplicacao ", multiplicacao)
print("divisao ", divisao)
