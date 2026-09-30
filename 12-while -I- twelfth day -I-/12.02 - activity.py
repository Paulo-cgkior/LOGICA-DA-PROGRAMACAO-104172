import os
os.system("cls")

while True:
    numero = int(input("Digite uma nota de 1 a 10: "))
    if numero < 0 or numero > 10:
        print ("Informe a sua nota novamente: ")
    else:
        print(f"Nota: {numero}")
        break

print("=Fim=")