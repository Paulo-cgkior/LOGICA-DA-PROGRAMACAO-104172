import os
os.system("cls")

altura = float(input("Informe a sua altura: "))
sexo = str(input("Informe M caso seja Masculino e informe F caso seja feminino: ")).lower()

match sexo:
    case "m":
        PesoM = (72.7 * altura) - 58
        print (PesoM)
    case "f":
        PesoF = (62.1 * altura) - 44.7
        print (PesoF)