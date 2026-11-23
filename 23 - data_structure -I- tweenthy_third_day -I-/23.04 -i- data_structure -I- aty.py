from dataclasses import dataclass
import os
os.system("cls")

# CRIE UMA CLASSE PARA UM PACIENTE
# Dados: nome, idade, telefone, endereço
# CRIE UMA FUNÇÃO PARA MOSTRAR:
# TODOS S DADOS
# NOME E IDADE
# NOME E TELEFONE
@dataclass
class Cliente:
    nome = str
    idade = str
    telefone = str
    endereco = str
    def mostrar_todos_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")

    def mostrar_nome_idade(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")

    def mostrar_nome_telefone(self):
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")

lista_cliente = []

print("= Solicitando dados =")
dados = Cliente(
    nome = input("Digite seu nome: "),
    idade = input("Digite sua idade: "),
    telefone = input("Digite seu telefone: "),
    endereco = input("Digite seu endereço: ")
    )
lista_cliente.append(dados)

print("\n= Exibindo dados =")
for cliente in lista_cliente:
    cliente.mostrar_todos_dados()

print("\n= Exibindo nome e idade =")
for cliente in lista_cliente:
    cliente.mostrar_nome_idade()

print("\n= Exibindo nome e telefone =")
for cliente in lista_cliente:
    cliente.mostrar_nome_telefone()