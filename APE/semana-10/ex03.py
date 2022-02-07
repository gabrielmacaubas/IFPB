"""
Escreva um programa que leia um vetor V contendo N elementos inteiros (N será
lido) e um valor inteiro K, verifique e exiba se o K está ou não no vetor. Se estiver,
informe em que posição (índice).
Obs: K pode se repetir no vetor, nesse caso, mostre todas as posições onde o K
aparece.
"""
a_tamanho = int(input("Digite o tamanho do vetor V: "))
a = [None] * a_tamanho

print("\nDigite os elementos do vetor A:")

for indice in range(a_tamanho):
    a[indice] = int(input(f"v[{indice}]:"))

k = int(input("\nDigite o valor de K: "))
contador = int()
posicoes = []

for indice in range(a_tamanho):
    if a[indice] == k:
        posicoes += [None]
        posicoes[contador] = indice
        contador += 1

if contador >= 1:
    print(f"\nO valor {k} está no vetor nas seguintes posições:")

    for pos in posicoes:
        print(pos)

else:
    print(f"\nO valor {k} não está no vetor")
