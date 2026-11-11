import os
os.system("cls")

loging = str("user")
senhag = str("senha")

login = str(input("Digite seu login: "))
senha = str(input("Digite sua senha: "))

if login == loging and senha == senhag:
    print ("login e senha corretos")
    print ("Bem vindo")
else:
    print ("login ou senha incorretos")
