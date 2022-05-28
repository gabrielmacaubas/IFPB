from random import randint
nlin = 2
ncol = 3

matriz = [[None]*ncol for i in range(nlin)]

for i in range(nlin):
    for j in range(ncol):
        matriz[i][j] = i + j

print("matriz")
for vetor in matriz:
    for elemento in vetor:
        print(f"{elemento:>4}", end="")
    print()

