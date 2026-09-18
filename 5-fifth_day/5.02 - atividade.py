import os
os.system("cls")

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
qfaltas = int(input("Digite sua quantidade de faltas: "))
media = (nota1 + nota2) / 2

if media >= 7.0 and qfaltas >= 40:
    print ("Aprovado")
else:
    print("Reprovado")