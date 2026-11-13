import os
os.system("cls")

# Função com parâmetros e retorno.
def calcular_notas(nota1, nota2):
    Resultado = nota1 + nota2
    return Resultado

print("= SOLICITANDO NOTAS =")
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

# Usando a Função com parâmetros e retorno.
# Inserindo o retorno na variavel soma
soma = calcular_notas(nota1, nota2)

print("= EXIBINDO NOTAS =")
print(f"Soma: {soma}")
