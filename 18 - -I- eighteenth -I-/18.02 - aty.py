import os
os.system("cls")

séries = []

while True:
    print(""" === Digite o numero da sua escolha ===
    
    1 - Adicionar série/s
    2 - Liste as séries
    0 - Encerrar

    """)

    opcao = int(input("Digite a sua opção: "))

    match opcao:
        case 1:
            print("Cadastrando uma série")
