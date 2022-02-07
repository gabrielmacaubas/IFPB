"""
Escreva um programa que leia um vetor de N números inteiros (N será lido),
inverta a ordem dos elementos do vetor e exiba o vetor invertido.
Ex: V = [1, 3, 5, 7], após a inversão: V = [7, 5, 3, 1].
Obs: É necessário inverter os elementos do vetor, não basta imprimi-los em
ordem inversa!
"""
vetor = [None] * int(input("Digite o tamanho do vetor: "))
vetor_tamanho = len(vetor)

print("Digite os 4 elementos do vetor:")

for elemento in range(vetor_tamanho):
    vetor[elemento] = int(input())

print(f"\nAntes da inversão: {vetor}")

vetor_temp = [None] * vetor_tamanho
cont = 0

for elemento in range(vetor_tamanho - 1, -1, -1):
    vetor_temp[cont] = vetor[elemento]
    cont += 1

for elemento in range(vetor_tamanho):
    vetor[elemento] = vetor_temp[elemento]

print(f"\nDepois da inversão: {vetor}")
