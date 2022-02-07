"""
Faça um programa que leia 3 números inteiros (N, X, Y) e mostre todos os
números múltiplos de N entre X e Y.
"""

n = int(input("Numero inteiro: "))
x = int(input("Numero inteiro: "))
y = int(input("Numero inteiro: "))

for c in range(x, y+1):

    if c % n == 0:
        print(c)
