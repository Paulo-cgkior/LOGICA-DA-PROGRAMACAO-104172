import os 
 #Limpo o terminal
os.system("cls")
    
# Entrada.
print("= SOLICITANDO DADOS =")
primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

#Processamento.
soma = primeiro_numero + segundo_numero
media = primeiro_numero + segundo_numero / 2
multiplicacao = primeiro_numero * segundo_numero

if primeiro_numero > segundo_numero:
   maior = primeiro_numero
   menor = segundo_numero

else:
    maior = primeiro_numero
    menor = segundo_numero

# Saida.
print("\n = EXIBINDO DADOS =")
print(f"soma:  {soma}")
print(f"media:  {media}")
print(f"produto:  {multiplicacao}")
print(f"Maior:  {maior}")
print(f"Menor:  {menor}")

