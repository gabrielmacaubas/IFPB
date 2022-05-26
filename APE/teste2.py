from random import randint

linhas_a = 2
colunas_a = 3

linhas_b = 3
colunas_b = 2

matriz_a = [[None] * colunas_a for i in range(linhas_a)]
matriz_b = [[None] * colunas_b for i in range(linhas_b)]

for l in range(linhas_a):
    for c in range(colunas_a):
        matriz_a[l][c] = randint(1, 10)
        print(matriz_a[l][c], end=" ")
    print()

print()
for l in range(linhas_b):
    for c in range(colunas_b):
        matriz_b[l][c] = randint(1, 10)
        print(matriz_b[l][c], end=" ")
    print()

matriz_c = [[None] * colunas_b for i in range(linhas_a)]

print()

for l in range(linhas_a):
    for c in range(colunas_b):
        for k in range(colunas_a):
            print(matriz_a[l][k], matriz_b[k][c])


