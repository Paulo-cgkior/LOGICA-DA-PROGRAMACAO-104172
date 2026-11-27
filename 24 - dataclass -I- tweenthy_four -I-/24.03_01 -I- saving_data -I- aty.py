from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class Clientes:
    nome: str
    email: str
    telefone: int
    endereco: str

lista_clientes = []

novo_cliente = Clientes(
    nome = input("Digite seu nome: "),
    email = input("Digite sua idade: "),
    telefone = int(input("Digite seu telefone: ")),
    endereco = input("Digite seu endereço: "))
lista_clientes.append(novo_cliente)

# Salvando o arquivo
arquivo = "dados_clientes.csv"
with open(arquivo, "w") as arquivo_clientes:
    for cliente in lista_clientes:
        arquivo_clientes.write(f"{cliente.nome}, {cliente.email}, {cliente.telefone}, {cliente.endereco}\n")

print("Cliente salvo com sucesso")