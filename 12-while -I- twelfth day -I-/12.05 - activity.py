import os
os.system("cls")

QUANTIDADE_TENTATIVAS = 3
LOGIN = "user"
SENHA = "1234"
tentativas = 1

while True:
    if tentativas <= 3:
        print (f"Tentativa: {tentativas}")
        login = str(input("Digite seu login: "))
        senha = str(input("Digite sua senha: "))
        tentativas += 1
        if login == LOGIN and senha == SENHA:
            print ("Bem vindo! ")
            break
        else:
            print ("Login ou senha inválidos")
            print ("Tente novamente! \n")
            input ("Pressione uma tecla para continuar...")
            os.system("cls")
    else:
        print(" =Fim= ")
        break