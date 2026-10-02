import os
os.system("cls")


while True:
    print(" | opção 1 | briar | 99,00")
    print(" | opção 2 | gwen  | 70,00")
    print(" | opção 3 | elise | 80,00")
    print(" | opção 4 | rengar| 50,00")
    print(" | opção 5 | udyr  | 35,00")

    print("")
    print("")

    escolha = int(input("Digite o número da sua opção: "))
    match escolha:
        case 1:
            print(" === Opção escolhida === ")
            print(" | opção 1 | briar | 99,00")
            break
        case 2:
            print(" === Opção escolhida === ")
            print(" | opção 2 | gwen  | 70,00")
            break
        case 3:
            print(" === Opção escolhida === ")
            print(" | opção 3 | elise | 80,00")
            break
        case 4:
            print(" === Opção escolhida === ")
            print(" | opção 4 | rengar| 50,00")
            break
        case 5:
            print(" === Opção escolhida === ")
            print(" | opção 5 | udyr  | 35,00")
            break
        case _:
            print("")
            print("Opção inválida")
            input("Aperte qualquer tecla para continuar...")
            os.system("cls")
