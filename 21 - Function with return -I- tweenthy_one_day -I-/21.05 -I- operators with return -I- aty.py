import os
os.system("cls")

def funcao_soma (numero1, numero2):
    resultado = numero1 + numero2
    return resultado
def funcao_subtracao (numero1, numero2):
    resultado = numero1 - numero2
    return resultado
def funcao_multiplicacao (numero1, numero2):
    resultado = numero1 * numero2
    return resultado
def funcao_divisao (numero1, numero2):
    if numero2 == 0:
        return "Atenção! Divisão por zero."
    return numero1 / numero2
print("= Recebendo dados =")
numero1 = int(input("\n Digite seu primeiro número: "))
numero2 = int(input("Digite seu segundo número: "))

soma = funcao_soma(numero1, numero2)
subtracao = funcao_subtracao(numero1, numero2)
multiplicacao = funcao_multiplicacao(numero1, numero2)
divisao = funcao_divisao(numero1, numero2)

print("\n= Exibindo Dados =")

print(f"Primeiro número: {numero1}")
print(f"Segundo número: {numero2}")
print(f"Soma: {soma}")
print(f"Subtracao: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")