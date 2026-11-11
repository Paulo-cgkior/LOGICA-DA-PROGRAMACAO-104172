import os
os.system("cls")

numero1 = int(input("Digite seu primeiro numero: "))
numero2 = int(input("Digite seu segundo numero: "))
operador = str(input("Digite o operador: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

match operador:
    case "+":
        Resultado = (soma)
    case "-":
        Resultado =  (subtracao)
    case "*":
        Resultado = (multiplicacao)
    case "/":
        Resultado =  (divisao)

print (f"Primeiro numero escolhido: {numero1}")
print (f"Segundo numero escolhido: {numero2}")
print (f"Operador escolhido: {operador}")
print (f"Resultado: {Resultado}")
