import os
os.system("cls")

#Entrada

peso = float(input("Digite seu Peso: "))
altura = float(input("Digite sua altura "))
imc =  peso / (altura * altura)

#Processamento

if imc <= 18.5:
    print ("Abaixo do peso")
elif imc <= 24.9:
    print ("Peso ideal (parabéns)")
elif imc <= 29.9:
    print ("Levemente acima do peso")
elif imc <= 34.9:
    print ("Obesidade grau I")
elif imc <= 39.9:
    print ("Obesidade grau II (Severa)")
else:
    print ("Obesidade grau III (Mórbida)")

#Saida

print (f"Peso do individuo: {peso}")
print (f"Altura do cidadão: {altura}")
print (f"IMC da pessoa: {imc:.3}")