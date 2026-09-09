import os
os.system("cls")

valor_do_produto = float(input("Digite o valor do produto: "))
Forma_de_Pagamento = int(input("Digite 1 caso o pagamento for a vista, "
"Digite 2 caso o pagamento for á prazo: "))

Total_com_desconto_de_10 = valor_do_produto / 100

match Forma_de_Pagamento:
    case 1:
        print (f"Valor do produto: {valor_do_produto}")
        print (f"Forma de pagamento: à vista")
        print (f"Valor do desconto: 10%")
        print (f"total a pagar ={valor_do_produto - Total_com_desconto_de_10}")
    case 2:
        parcelas = int(input("Informe o número de parcelas entre 1 a 6 que deseja pagar: "))
        parcelado = valor_do_produto / parcelas
        print (f"Valor do produto: {valor_do_produto}")
        print (f"Forma de pagamento: à prazo")
        print (f"Quantidade de parcelas: {parcelas}")
        print (f"total a pagar ={parcelado}")
