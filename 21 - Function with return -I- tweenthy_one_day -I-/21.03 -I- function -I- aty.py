import os
os.system("cls")

def resultado_final(numero):
    if numero % 2 == 0:
        resultado = "par"
    elif numero % 2 == 1:
        resultado = "impar"
    return resultado

print ("= SOLICITANDO DADOS =")
numero = int(input("Digite um número: "))
resultado = resultado_final(numero)

os.system("cls")

print ("= EXIBINDO DADOS =")
print (f"\nExibindo o número escolhido: {numero}")
print ("\nO número é impar ou par?")
print (f"O número é: {resultado}")