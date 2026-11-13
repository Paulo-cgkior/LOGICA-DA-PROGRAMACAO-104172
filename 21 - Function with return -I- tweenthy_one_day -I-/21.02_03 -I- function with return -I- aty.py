import os
os.system("cls")

# Função com parâmetros e retorno.
def calcular_notas(nota1, nota2):
    resultado = (nota1 + nota2) / 2
    return resultado

def verificar_resultado(media):
    if media >= 7:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"
    return resultado

print("= SOLICITANDO NOTAS =")
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

# Usando a Função com parâmetros e retorno.
# Inserindo o retorno na variavel soma
media = calcular_notas(nota1, nota2)
situação = verificar_resultado(media)

print("= EXIBINDO NOTAS =")
print(f"Soma: {media}")
print(f"Aprovação: {situação}")

