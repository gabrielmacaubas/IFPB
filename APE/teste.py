linhas = 10
colunas = 9
matriz = [[0] * colunas for i in range(linhas)]

print("Informe o local de cada acidente\nPara encerrar, digite 0 para a Av.")

while True:
    avenida = int(input("\nAv. (1 a 10): "))
    if avenida == 0:
        break
    rua = int(input("Rua (30 a 38): "))

    matriz[avenida-1][rua-30] += 1

print("\nMAPA DOS ACIDENTES")
print("\nRua/Av.  30  31  32  33  34  35  36  37  38")

for l in range(linhas):
    print(f"{l+1:^7}", end="")
    for c in range(colunas):
        if matriz[l][c] == 0:
            print(f"{'-':>4}", end="")

        else:
            print(f"{matriz[l][c]:>4}", end="")

    print()
"""
1 2 3
4 5 6

7 8 9
10 11 12

x x x
x x x

"""