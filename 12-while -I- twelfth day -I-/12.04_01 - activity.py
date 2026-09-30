import os
import time
os.system("cls")

LOGIN = "joao"
SENHA = "1234"

#Caso precise colocar no banco de dados
#LOGIN = str(input("Digite seu login: "))
#SENHA = int(input("Digite sua senha: "))

while True:
    login = str(input("Digite seu login: "))
    senha = str(input("Digite sua senha: "))

    if login == LOGIN and senha == SENHA:
        print("")
        print (f"Login: {login}")
        print (f"Senha: {senha}")
        break
    else:
        print("Dados incorretos")
        print("")
        input("Pressione uma tecla para continuar...")
        os.system("cls")