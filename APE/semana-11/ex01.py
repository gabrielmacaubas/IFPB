"""
Escreva um programa que leia um vetor contendo N elementos inteiros (N será
lido), calcule e exiba:
• A quantidade de elementos pares;
• A quantidade de elementos ímpares;
• A soma de todos os elementos;
• A média dos elementos do vetor.
"""
n = int(input("Digite o valor de N: "))
vetor = [None] * n
pares = int()
impares = int()
soma = int()

print("\nDigite os elementos do vetor:")

for number in range(n):
    vetor[number] = int(input())

    if vetor[number] % 2 == 0:
        pares += 1

    else:
        impares += 1

    soma += vetor[number]

media = soma / len(vetor)

print(f"Quantidade de elementos pares: {pares}")
print(f"Quantidade de elementos ímpares: {impares}")
print(f"Soma de todos os elementos {soma}")
print(f"Média dos elementos: {media:.0f}")
