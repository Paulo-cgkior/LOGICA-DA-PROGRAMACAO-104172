import os
os.system("cls")

primeira_nota = float(input("sua_primeira_nota: "))
segunda_nota = float(input("sua_segunda_nota: "))
terceira_nota = float(input("sua_terceira_nota: "))

media = (primeira_nota + segunda_nota + terceira_nota) / 3
if media >= 7:
    print("Aluno Passou")
else:
    print ("Aluno perdeu:")
print (f"Resultado: {media:.2f}")