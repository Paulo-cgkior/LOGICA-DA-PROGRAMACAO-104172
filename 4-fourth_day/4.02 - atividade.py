import os
os.system("cls")

#Entrada

nome_do_aluno = str(input("Digite o nome do aluno: "))
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
media = (nota_1 + nota_2) / 2

#Processamento

if media < 4:
    print ("Reprovado (E)")
elif media < 6:
    print ("Reprovado (D)")
elif media <= 7.5:
    print ("Aprovado (C)")
elif media < 9:
    print ("Aprovado (B)")
else:
    print ("Aprovado (A)")

#Saida
print (f"nome do aluno: {nome_do_aluno}")
print (f"Media: {media}")