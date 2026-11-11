import os

# FAÇA UM PROGRAMA COM MATCH CASE.
# 1 - CADASTRAR CLIENTE
# 2 - MOSTRAR DADOS DO CLIENTE
# 3 - SAIR

# FAÇA A FUNÇÃO PARA CADASTRAR SER USADA NO CASE 1:
# FAÇA A FUNÇÃO PARA MOSTRAR DADOS DO CLIENTE SER USADA NO CASE 2:
# CASE 3 USE A FUNÇÃO exit() para sair
# CASE _: PARA OPÇÕES INCORRETAS

def mostrar_dados(nome, idade, telefone):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Email: {telefone}")


while True:
    os.system("cls")
    print (" 1 - CADASTRAR CLIENTE ")
    print (" 2 - MOSTRAR DADOS DO CLIENTE")
    print (" 3 - SAIR")

    escolha = int(input("Digite sua escolha: "))
    match escolha:
        case 1:
            # cadastrar cliente
            nome = input("Digite seu nome: ")
            idade = input("Digite sua idade: ")
            telefone = input("Digite seu telefone: ")
            input("Digite enter para continuar...")
        case 2:
            # Mostrar dados do cliente
            mostrar_dados(nome, idade, telefone)
            input("Digite enter para continuar...")
        case 3:
            # Sair
            print("Saindo do programa... ")
            exit()
        case _:
            # Opções invalidas
            print("Dados inseridos invalidos")
            input("Digite enter para continuar...")
