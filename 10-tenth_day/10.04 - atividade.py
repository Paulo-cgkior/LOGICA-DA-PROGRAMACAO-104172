import os
import time
os.system("cls")

numero = int(input("Digite seu número: "))

for numero in range(numero, 0, -1):
    print(numero)
    time.sleep(1)