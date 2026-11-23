from dataclasses import dataclass
import os
os.system("cls")

# CRIE UMA CLASSE PARA OS DADOS DE UM CLIENTE
@dataclass
class Cliente:
    nome: str
    telefone: str
    email: str

    #FUNÇÃO DENTRO DA CLASSE
    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"E-mail: {self.email}")
        print("="*30)

    #FUNÇÃO DENTRO DA CLASSE
    def email_marketing(self):
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print("="*30)

    #Função somente para enviar whatzapp.
    def whatsapp_marketing(self):
        print(f"Nome: {self.nome}")
        print(f"Whatsapp: {self.telefone}")
        print("="*30)       

lista_cliente = []

print("= SOLICITANDO DADOS = ")
for i in range(2):
    dados = Cliente(
        nome = input("\nDigite o nome do cliente: "),
        telefone = input("Digite o telefone do cliente: "),
        email = input("Digite o e-mail do cliente: ")
    )
    lista_cliente.append(dados)

print("\n= EXIBINDO DADOS =")
for cliente in lista_cliente:
    cliente.mostrar_dados()

    print("\n= EXIBINDO E-MAIL MARKETING =")
for cliente in lista_cliente:
    cliente.email_marketing()

    print("\n= EXIBINDO WHATSAPP =")
for cliente in lista_cliente:
    cliente.whatsapp_marketing()