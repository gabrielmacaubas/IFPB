"""
Escreva um programa que:
• Leia (ou gere aleatoriamente) uma matriz quadrada de ordem N contendo elementos
inteiros (N será lido);
• Exiba a matriz lida (no formato de matriz);
• Exiba os elementos da diagonal principal, isto é, os elementos onde I = J.
"""
n = int(input("Digite a ordem da matriz: "))
matriz = [[None] * n for i in range(n)]
diagonal = [None] * n

print("Digite os elementos da matriz:")

for l in range(n):
    for c in range(n):
        matriz[l][c] = int(input(f"m{[l]}{[c]}: "))

        if l == c:
            diagonal[l] = matriz[l][c]

print(f"\nMatriz:")

for l in matriz:
    for c in l:
        print(f"{c:4}", end="")

    print()

print("\nDiagonal Principal:")

for d in diagonal:
    print(f"{d:4}", end="")
