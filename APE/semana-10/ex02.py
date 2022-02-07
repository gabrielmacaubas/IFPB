"""
Escreva um programa que leia um vetor V (contendo 30 inteiros) e um valor
inteiro K, calcule e exiba a quantidade de ocorrências de K dentro de V.
"""
print("Digite os elementos do vetor A:")

a_tamanho = 5
a = [None] * a_tamanho

for number in range(a_tamanho):
    a[number] = int(input())

k = int(input("Digite o valor de K: "))
k_ocorrencias = int()

for number in a:
    if number == k:
        k_ocorrencias += 1

print(f"\nNº de ocorrências: {k_ocorrencias}")
