import os
os.system("cls")

# Entrada.
print("= SOLICITANDO DADOS =")
primeiro_numero = float(input("Digite o numero A: "))
segundo_numero = float(input("Digite o numero B: "))
operador = str(input("Digite o seu operador matematico: "))

#Processamento.
soma = primeiro_numero + segundo_numero
subtracao = primeiro_numero - segundo_numero
multiplicacao = primeiro_numero * segundo_numero
divisao = primeiro_numero / segundo_numero

match operador:
    case "+":
        print (f"a soma dos numeros {primeiro_numero} + {segundo_numero} = {soma}")
    case "-":
        print (f"a subtração dos numeros {primeiro_numero} - {segundo_numero} = {subtracao}")
    case "*":
        print (f"a multiplicação dos numeros {primeiro_numero} * {segundo_numero} = {multiplicacao}")
    case "/":
        print (f"a Divisão dos numeros {primeiro_numero} / {segundo_numero} = {divisao}")
