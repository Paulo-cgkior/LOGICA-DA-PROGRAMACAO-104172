import os
os.system("cls")

#Sao numeros
A = float(input("Digite a variavel A: "))
B = float(input("Digite a variavel B: "))

if A == B:
    C = A + B
    print (f"soma entre A e B: {C}")
else:
    C = A * B
    print (f"multiplicação entre A e B: {C}")