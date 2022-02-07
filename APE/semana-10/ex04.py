"""
Escreva um programa que leia 10 números e armazene-os em um vetor. Exiba:
• Os números que estão nos índices pares;
• Os números que estão nos índices ímpares.
"""
vetor_tamanho = 10
vetor = [None] * vetor_tamanho

for elemento in range(vetor_tamanho):
    vetor[elemento] = int(input(f"numero[{elemento}]: "))

print("\nNúmeros que estão nos índices pares:")

for elemento in range(vetor_tamanho):
    if elemento % 2 == 0:
        print(vetor[elemento])

print("\nNúmeros que estão nos índices ímpares:")

for elemento in range(vetor_tamanho):
    if elemento % 2 != 0:
        print(vetor[elemento])
