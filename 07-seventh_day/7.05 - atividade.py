import os
os.system("cls")

print ("           === Cardápio ===         ")
print (" Codigo |       Prato          | Valor")
print ("   1    |      Picanha         | 25,00")
print ("   2    |      Lasanha         | 20,00")
print ("   3    |     Strogonoff       | 18,00")
print ("   4    |    Bife acebolado    | 15,00")
print ("   5    |     Pão com ovo      | 5,00")

codigo = int(input("Digite o numero do codigo do prato: "))

match codigo:
    case 1:
        print ("  Picanha         | 25,00")
    case 2:
        print ("  Lasanha         | 20,00")
    case 3:
        print ("  Strogonoff       | 18,00")
    case 4:
        print ("  Bife acebolado    | 15,00")
    case 5:
        print ("  Pão com ovo      | 5,00")
    case _:
        print ("Pedido invalido")