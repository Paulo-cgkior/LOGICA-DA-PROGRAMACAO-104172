import os
os.system("cls")

print ("    Cor      |   Preço  |")
print ("   verde     |  R$10,00 |")
print ("    Azul     |  R$20,00 |")
print ("   Amarelo   |  R$30,00 |")
print ("  Vermelho   |  R$40,00 |")

cor = str(input("Digite a cor do disco: ")).lower()

match cor:
    case "verde":
        print ("   verde     |  R$10,00 |")
    case "Azul":
        print ("    Azul     |  R$20,00 |")
    case "Amarelo":
        print ("   Amarelo   |  R$30,00 |")
    case "vermelho":
        print ("  Vermelho   |  R$40,00 |")

