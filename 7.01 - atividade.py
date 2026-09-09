import os
from datetime import date
os.system("cls")


Codigo_do_empregado = int(input("Digite o codigo do empregado: "))
ano_de_nascimento = int(input("Digite o ano de nascimento: "))
anos_trabalhados = int(input("Anos trabalhados pelo funcionario: "))

idade = date.today().year - ano_de_nascimento


print(f"Codigo do empregado: {Codigo_do_empregado}")
print(f"idade do empregado: {idade}")
print(f"Tempo em anos do empregado: {anos_trabalhados}")

if idade >= 65 and anos_trabalhados >= 30:
    Resultado = ("Requerer aposentadoria")
else:
    Resultado = ("Não requerer aposentadoria")

