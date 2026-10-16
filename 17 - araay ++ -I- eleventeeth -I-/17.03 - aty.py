import os
os.system("cls")

preco = 0
prato = ""
prato_vet = []
preco_vet = []

while True:
    print(" | opção 1 | briar | 99,00")
    print(" | opção 2 | gwen  | 70,00")
    print(" | opção 3 | elise | 80,00")
    print(" | opção 4 | rengar| 50,00")
    print(" | opção 5 | udyr  | 35,00")
    print(" | opção 6 | Encerrar o serviço")

    print("")
    print("")

    escolha = int(input("Digite o número da sua opção: "))

    match escolha:
        case 1:
            preco += 99
            prato = "briar"
            preco_vet.append(preco)
            print(" === Opção escolhida === ")
            print(" | opção 1 | briar | 99,00")
            print("")
        case 2:
            preco += 70
            prato = "gwen"
            preco_vet.append(preco)
            print(" === Opção escolhida === ")
            print(" | opção 2 | gwen  | 70,00")
        case 3:
            preco += 80
            prato = "elise"
            preco_vet.append(preco)
            print(" === Opção escolhida === ")
            print(" | opção 3 | elise | 80,00")
        case 4:
            preco += 50
            prato = "rengar"
            preco_vet.append(preco)
            print(" === Opção escolhida === ")
            print(" | opção 4 | rengar| 50,00")
        case 5:
            preco += 35
            prato = "udyr"
            preco_vet.append(preco)
            print(" === Opção escolhida === ")
            print(" | opção 5 | udyr  | 35,00")
        case _:
            print("")
            print("Opção inválida")
            input("Aperte qualquer tecla para continuar...")
            os.system("cls")
    escolhayn = str(input("Deseja escolher mais um prato?(Y/N)")).upper()
    if escolhayn == "Y":
        print("")
    elif escolhayn == "N":
        for i in enumerate(prato):
            print(f"{i + 1}º prato: {prato}")
            print(f"{i + 1}º preco: {preco}")
        print(f"preco: {preco}")
        break
    else:
        print("Comando inválido")
        input("Digite qualquer tecla para continuar...")