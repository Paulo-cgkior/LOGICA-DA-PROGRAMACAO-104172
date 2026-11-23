from dataclasses import dataclass
import os
os.system("cls")

# CRIE UMA CLASSE PARA OS DADOS DE UM CLIENTE
@dataclass
class Cliente:
    nome: str
    telefone: str
    e_mail: str

lista_cliente = []

# DADOS: NOME, TELEFONE E E-MAIL
dados_do_cliente = Cliente(
nome = input("\nDigite o nome do cliente: "),
telefone = str(input("\nDigite o telefone do cliente: ")),
e_mail = str(input("\nDigite o e-mail do cliente: "))
)
lista_cliente.append(dados_do_cliente)

print("\nEXIBINDO DADOS")
for cliente in lista_cliente:
    print(f"Nome: {cliente.nome}")
    print(f"Telefone: {cliente.telefone}")
    print(f"E-Mail: {cliente.e_mail}")
    print("="*15)