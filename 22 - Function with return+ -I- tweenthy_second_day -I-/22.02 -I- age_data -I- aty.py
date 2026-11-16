import os
from datetime import date
os.system("cls")

def idade_ano (ano):
    idade = date.today().year - ano
    return idade

print("= SOLICITANDO DADOS =")
ano = int(input("\nDigite o ano do seu nascimento: "))

resultado = idade_ano(ano)

print("= EXIBINDO DADOS =")
print(f"\nAno de nascimento: {ano}")
print(f"Ano atual: {date.today().year}")
print(f"Sua idade é: {resultado}")