import os
os.system("cls")

A = float(input("Digite a variável A: "))
B = float(input("Digite a variável B: "))
C = float(input("Digite a variável C: "))

soma = A + B

if soma < C:
    print ("A soma de A + B é menor que C")
else:
    print ("A soma de A + B é maior que C")

print (f"Variavel A: {A}")
print (f"Variavel B: {B}")
print (f"Variavel C: {C}")