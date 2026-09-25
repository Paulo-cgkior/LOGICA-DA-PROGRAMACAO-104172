import os
os.system("cls")

print("== MOSTRANDO NUMEROS IMPARES ==")
for i in range(1, 20):
    if i % 2 == 1:
        print(i)

print("")
print("== MOSTRANDO NUMEROS IMPARES ==")
for i in range(1, 20, 2):
    print(i)
