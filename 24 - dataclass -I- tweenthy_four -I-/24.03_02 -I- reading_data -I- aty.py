from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class Clientes:
    nome: str
    email: int
    telefone: int
    endereco: str

lista_clientes = []

# Lendo o arquivo
arquivo = "dados_clientes.csv"
with open(arquivo, "r") as arquivo_clientes:
    for linha in arquivo_clientes:
        nome, email, telefone, endereco = linha.strip().split(',')
        lista_clientes.append(Clientes(
            nome = nome,
            email = email,
            telefone = int(telefone),
            endereco = endereco
        ))

print("= Exibindo dados do cliente =")
for cliente in lista_clientes:
    print(f"nome: {cliente.nome}")
    print(f"email: {cliente.email}")
    print(f"telefone: {cliente.telefone}")
    print(f"endereco: {cliente.endereco}")
    print("="*15)