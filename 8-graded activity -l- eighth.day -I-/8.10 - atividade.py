import os
os.system("cls")

print (" Combustivel |      Quantidade vendida       | Desconto por litro")
print ("   Álcool    |       Até 25 litros           |       10%         ")
print ("   Álcool    |       Acima de 25 litros      |       20%         ")
print ("  Gasolina   |       Até 25 litros           |       15%         ")
print ("  Gasolina   |       Acima de 25 litros      |       30%         ")

combustível = str(input("Digite (A) para alcool e (G) para gasolina: ")).lower()
litros = int(input("Digite quantos litros deseja: "))
valor_alcool = 3.78
valor_gasolina = 6.59

match combustível:
    case "A":
        valorA = valor_alcool * litros
        if litros <= 25:
            print (f"Valor a pagar no alcool: {valorA / 0.10}")
        else:
            print (f"Valor a pagar no alcool: {valorA / 0.20}")
    case "G":
        valorG = valor_gasolina * litros
        if litros <= 25:
            print (f"Valor a pagar na gasolina: {valorG / 0.15}")
        else:
            print (f"Valor a pagar na gasolina: {valorG / 0.30}")