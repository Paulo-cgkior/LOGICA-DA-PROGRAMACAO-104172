import os
os.system("cls")

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))
terceiro_numero = int(input("Digite o seu terceito número: "))

menor = min(primeiro_numero, segundo_numero, terceiro_numero)
maior = max(primeiro_numero, segundo_numero, terceiro_numero)

print(f"Numeros informados: {primeiro_numero} , {segundo_numero}, {terceiro_numero}")
print(f"O maior número:  {maior}")
print(f"O Menor número:  {menor}")

# if primeiro_numero > segundo_numero:
#   maior = primeiro_numero
#   menor = segundo_numero
# else:
#    maior = segundo_numero
#    menor = primeiro_numero