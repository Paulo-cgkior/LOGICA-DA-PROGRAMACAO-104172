 #Limpo o terminal
import os
os.system("cls")
    
# Entrada.
print("= SOLICITANDO DADOS =")
primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

#Processamento.
soma = primeiro_numero + segundo_numero
media = primeiro_numero + segundo_numero / 2
produto = primeiro_numero * segundo_numero

if primeiro_numero > segundo_numero:
   maior = primeiro_numero
   menor = segundo_numero

else:
    maior = segundo_numero
    menor = primeiro_numero

outro_maior = max(primeiro_numero, segundo_numero)
outro_menor = min(primeiro_numero, segundo_numero)

# Saida.
print("\n = EXIBINDO DADOS =")
print(f"soma:  {soma}")
print(f"media:  {media}")
print(f"produto:  {produto}")
print(f"Maior:  {maior}")
print(f"Menor:  {menor}")
print(f"segundo Maior:  {outro_maior}")
print(f"terceiro Menor:  {outro_menor}")

if primeiro_numero == segundo_numero:
    print("Numeros iguais")
else:
    print("Não são iguais")

