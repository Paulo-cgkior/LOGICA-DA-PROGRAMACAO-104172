import os
from datetime import date
os.system("cls")

print ("== Informe entre MASCULINO E FEMININO em letras maiusculas ==")
sexo_de_registro = str(input("Digite o sexo de registro: "))
ano_de_nascimento = int(input("Digite o ano de nascimento: "))
idade = date.today().year - ano_de_nascimento

if sexo_de_registro == "MASCULINO" and idade == 18:
    Resultado = ("Serviço militar obrigatorio")
else:
    Resultado = ("Usuario não deverá se apresentar")

print (Resultado)