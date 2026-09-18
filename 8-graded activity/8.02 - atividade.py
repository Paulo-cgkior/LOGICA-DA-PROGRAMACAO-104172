import os
os.system("cls")

nome = str(input("Digite seu nome: "))
sexo = str(input(f"Digite (M) para Masculino ou (F) para feminino): ")).lower()
estado_civil = str(input("Digite seu estado civil: ")).lower()

print (f"Nome: {nome}")
print (f"Sexo: {sexo}")
print (f"Estado civil: {estado_civil}")

if estado_civil == "casada" and sexo == "f":
    tempo_de_casada = int(input("Digite o tempo de casado(a): "))
    print (f"Tempo de Casada): {tempo_de_casada}")
