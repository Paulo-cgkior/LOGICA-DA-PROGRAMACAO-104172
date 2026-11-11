import os
os.system("cls")

print("= Tabuada =")
numero = int(input("Digite um número: "))

#
for i in range(1, 11):
    print (" Soma ")
    print (f"{numero} + {i} = {numero + i}")
#
for i in range(1, 11):
    print (" Subtração ")
    print (f"{numero} - {i} = {numero - i}")
#
for i in range(1, 11):
    print (" Multiplicação ")
    print (f"{numero} * {i} = {numero * i}")
#
for i in range(1, 11):
    print (" Divisão ")
    print (f"{numero} / {i} = {numero / i}")