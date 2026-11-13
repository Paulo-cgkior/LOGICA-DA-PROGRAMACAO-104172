import os
os.system("cls")

def metros_centimetros(numero):
    resultado = numero * 100
    return resultado

print("= Solicitando Dados =")
numero = float(input("\nDigite seu número: "))

centimetros = metros_centimetros(numero)

print("\n= Exibindo Resultados =")
print(f"Número escolhido: {numero}")
print(f"Valor em centimetros: {centimetros}")