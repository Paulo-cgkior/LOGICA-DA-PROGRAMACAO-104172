import os
os.system("cls")

print (" Fruta   |       Até 5kg       | Acima de 5kg")
print (" Morango |   R$ 2,25 por kg    | R$2,20 por kg")
print (" Maçã    |   R$ 1,80 por kg    | R$1,50 por kg")

fruta = str(input("Digite a fruta desejada: "))


match fruta:
    case "morango":
        morangokg = float(input("Digite a quantidade de kg escolhida: "))
        if morangokg <= 5:
            Valormo = 2.50
        else:
            Valormo = 2.20
        desconto = Valormo * 0.10
        if Valormo >= 15 or morangokg >= 10:
            print (f"Valor a pagar: {(morangokg * Valormo) - desconto} ")
        else:
            print (f"Valor a pagar: {(morangokg * Valormo)} ")

    case "maçâ":
        macakg = float(input("Digite a quantidade de kg escolhida: "))
        if macakg <= 5:
            Valorma = 1.80
        else:
            Valorma = 1.50
        desconto = Valorma * 0.10
        if Valorma >= 15 or macakg >= 10:
            print (f"Valor a pagar: {(macakg * Valorma) - desconto} ")
        else:
            print (f"Valor a pagar: {(macakg * Valorma)} ")
