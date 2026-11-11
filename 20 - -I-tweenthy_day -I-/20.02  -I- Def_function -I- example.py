import os
os.system("cls")

# Criando uma função.
def cabeçalho():
    print("\n")
    print ("="*15)
    print ("    SENAI")
    print ("="*15)
    return

cabeçalho() # Usando a função.
nome = input("Digite seu nome: ")

cabeçalho() # Usando a função.
idade = input("Digite sua idade: ")

cabeçalho() # Usando a função.
print(f"Nome: {nome}")
print(f"Idade: {idade}")
