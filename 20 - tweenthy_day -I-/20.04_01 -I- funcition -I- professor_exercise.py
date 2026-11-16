import os
os.system("cls")

def logo_senai():
    os.system("cls")
    print("\n===============")
    print(" Senai - Bahia")
    print("\n===============")

def mostrar_dados(nome, email, telefone):
    print(f"Nome: {nome}")
    print(f"Email: {email}")
    print(f"Telefone: {telefone}")

logo_senai()
print("= SOLICITANDO DADOS =")
nome = input("Digite seu nome: ")

logo_senai()
print("= SOLICITANDO DADOS =")
email = input("Digite seu email: ")

logo_senai()
print("= SOLICITANDO DADOS =")
telefone = input("Digite seu telefone: ")

logo_senai()
print("\n= EXIBINDO DADOS =")
mostrar_dados(nome, email, telefone)



