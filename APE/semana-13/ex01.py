"""
Escreva um programa que preencha duas matrizes (A e B), ambas de ordem 2x3, com
valores inteiros fornecidos pelo usuário (ou gerados aleatoriamente). O programa
deverá somar as duas matrizes, armazenando o resultado em uma terceira matriz (C).
Ao final, exiba as 3 matrizes (no formato de matriz).
"""
linhas = 2
colunas = 3
matriz_a = [[None]*colunas for i in range(linhas)]
matriz_b = [[None]*colunas for i in range(linhas)]

print("nDigite os elementos de A:")

for l in range(linhas):
    for c in range(colunas):
        matriz_a[l][c] = int(input(f"[{l}][{c}]"))

print("\nDigite os elementos de B:")

for l in range(linhas):
    for c in range(colunas):
        matriz_b[l][c] = int(input(f"[{l}][{c}]"))

print("\nMatriz A:")

for l in matriz_a:
    for c in l:
        print(f"{c:4}", end='')
    print()

print("\nMatriz B:")

for l in matriz_b:
    for c in l:
        print(f"{c:4}", end='')
    print()

matriz_c = [[None]*colunas for i in range(linhas)]

for l in range(linhas):
    for c in range(colunas):
        matriz_c[l][c] = matriz_a[l][c] + matriz_b[l][c]

print("\nMatriz C:")

for l in matriz_c:
    for c in l:
        print(f"{c:4}", end='')
    print()
