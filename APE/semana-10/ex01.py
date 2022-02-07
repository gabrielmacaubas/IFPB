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
qtd_pares = int()

print("\nDigite os elementos do vetor: ")

for elemento in range(n):
    vetor[elemento] = int(input())

qtd_par = int()
qtd_impar = int()
soma = int()

for elemento in vetor:
    if elemento % 2 == 0:
        qtd_par += 1

    else:
        qtd_impar += 1

    soma += elemento

media = soma / len(vetor)

print(f"\nQuantidade de elementos pares: {qtd_par}")
print(f"Quantidade de elementos ímpares: {qtd_impar}")
print(f"Soma de todos os elementos: {soma}")
print(f"Média dos elementos: {media:.0f}")
