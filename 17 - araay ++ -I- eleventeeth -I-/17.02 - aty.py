import os
os.system("cls")

num_vet = []

for i in range(5):
    num = int(input(f"Digite o {i + 1}º número: "))
    if num < 0:
        num = 0
        num_vet.append(num)
    else:
        num_vet.append(num)

for i, num in enumerate(num_vet):
    print(f"{i + 1}º número: {num}")