import os
os.system("cls")

# FAÇA UM PROGRAMA QUE SOLICITE:
# - NOME, EMAIL E TELEFONE

def logo_senai():
    print("="*15)
    print("  Senai - Bahia  ")
    print("="*15)

def mostrar_dados(nome, email, telefone):
    print(f"Nome: {nome}")
    print(f"Email: {email}")
    print(f"Telefone: {telefone}")

# O PROGRAMA DEVE MANTER NA TELA O LOGO:
# =================
#   SENAI - BAHIA
# =================
# O LOGO DEVE ER EXIBIDO USANDO A FUNÇÃO:
# logo_senai()

logo_senai()
nome = input("Digite seu nome: ")

logo_senai()
email = input("Digite seu email: ")

logo_senai()
telefone = input("Digite seu telefone: ")

# OS DADOS DEVERÃO SER APRENTADOS POR MEIO
# DE UMA FUNÇÃO COM PARÂMETROS CHAMADA:
# mostrar_dados(nome, email, telefone)

mostrar_dados(nome, email, telefone)



