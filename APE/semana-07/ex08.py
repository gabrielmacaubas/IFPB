"""
Faça um programa que leia um número inteiro N, calcule e mostre o maior
quadrado perfeito menor ou igual a N. Por exemplo, se N for igual a 38, o
resultado é 36.
"""

n = int(input("numero inteiro: "))
quadrado_perfeito = int()

for c in range(1, n+1):
    if c * c <= n:
        quadrado_perfeito = c * c

print(quadrado_perfeito)
