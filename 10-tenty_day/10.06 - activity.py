import os
os.system("cls")

print("Mostrando os números pares entre 1 e 10")
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} é par.")
    else:
        print(f"{i} é impar")
print("FIM")