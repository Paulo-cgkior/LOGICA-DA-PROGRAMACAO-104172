import os
os.system("cls")

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = (nota1 + nota2) / 2

if media <= 4.0:
    print ("Aluno Rerovado")
elif media <= 5.9:
    print ("Aluno em recuperação")
elif media > 5.9:
    print ("Aluno Aprovado")
