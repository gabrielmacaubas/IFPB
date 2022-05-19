"""
Escreva um programa que gere aleatoriamente uma matriz quadrada A (cuja ordem
será lida) e gere uma matriz B (da mesma ordem de A), onde cada elemento de B
corresponderá ao respectivo elemento de A somado a ele os seus índices, sendo que se
o elemento for de alguma diagonal (principal ou secundária) deverá ser colocado 0
(zero).
Veja o exemplo a seguir:

Ao final, imprima as duas matrizes (no formato de matriz).
"""
import random

o = int(input("Ordem das matrizes: "))
matriz_a = [[None] * o for i in range(o)]
matriz_b = [[None] * o for i in range(o)]

print("Matriz A")

# criação da matriz A
for l in range(o):
    for c in range(o):
        matriz_a[l][c] = random.randint(1, 30)

        print(f"{matriz_a[l][c]:3}", end="")

    print()

print("\nMatriz B")

# criação da matriz B
for l in range(o):
    for c in range(o):
        matriz_b[l][c] = matriz_a[l][c] + (c + 1)

# remoção das diagonais
for l in range(o):
    for c in range(o):
        # remoção da diagonal principal
        if l == c:
            matriz_b[l][c] = 0
    
    # remoção da diagonal secundária
    matriz_b[l][(o - 1) - l] = 0

# impressão
for l in matriz_b:
    for c in l:
        print(f"{c:3}", end="")

    print()
