import os
os.system("cls")

def tabuada_soma(numero):
    for i in range(1, 11):
        print (f"{i} + {numero} = {i + numero}")
def tabuada_subtracao(numero):
    for i in range(1, 11):
        print (f"{i} - {numero} = {i - numero}")
def tabuada_multiplicacao(numero):
    for i in range(1, 11):
        print (f"{i} x {numero} = {i * numero}")
def tabuada_divisao(numero):
    for i in range(1, 11):
        print (f"{i} / {numero} = {i / numero}")


numero = int(input("Digite seu número: "))

opcao = input('Digite a tabuada q c qr: ')
match opcao:
    case '+':
        tabuada_soma(numero)
    case '-':
        tabuada_subtracao(numero)
    case 'x':
        tabuada_multiplicacao(numero)
    case '/':
        tabuada_divisao(numero)
    case _:
        print('equação inválida')