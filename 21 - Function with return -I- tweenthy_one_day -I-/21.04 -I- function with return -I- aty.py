import os
os.system("cls")

def result_neg_pos (numero):
    if numero > 0:
        resultado = "Positivo"
    elif numero == 0:
        resultado = "neutro"
    else:
        resultado = "Negativo"
    return resultado

print("= RECEBENDO DADOS=")
numero = int(input("\nDigite seu número: "))

resultado_num = result_neg_pos(numero)

print("\n= EXIBINDO RESULTADOS =")
print(f"\n Número escolhido: {numero} é {resultado_num  }")