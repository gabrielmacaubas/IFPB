"""
Uma matriz transposta é a matriz que se obtém da troca de linhas por colunas de uma
dada matriz.
Assim, dada uma matriz C de ordem m x n, a matriz transposta dela será representada
por Ct de ordem n x m, onde cada elemento de Ct[i,j] = C[j,i].

Escreva um programa que preencha uma matriz 3x5 com valores inteiros fornecidos
pelo usuário (ou gerados aleatoriamente) e gere a sua transposta. Ao final, imprima as
duas matrizes (no formato de matriz).
"""
print("Digite os elementos da matriz M:")

linhas = 2
colunas = 3
matriz_c = [[None] * colunas for i in range(linhas)]
ct = [[None] * linhas for i in range(colunas)]

for l in range(linhas):
    for c in range(colunas):
        matriz_c[l][c] = int(input(f"M[{l}][{c}]: "))

print("\nMatriz M:")

for l in matriz_c:
    for c in l:
        print(f"{c:4}", end="")

    print()

for l in range(linhas):
    for c in range(colunas):
        ct[c][l] = matriz_c[l][c]

print("\nMatriz T (transposta):")

for l in ct:
    for c in l:
        print(f"{c:4}", end="")

    print()
