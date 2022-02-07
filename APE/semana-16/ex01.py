"""
Escreva uma função chamada menor que receba 3 números e retorne o menor
deles. Faça também um programa para testar a função.
"""


def menor(x, y, z):
    if x < y and x < z:
        return x

    elif y < x and y < z:
        return y

    else:
        return z


print("Informe 3 valores distintos")

n1 = int(input("1° valor:"))
n2 = int(input("2° valor:"))
n3 = int(input("3° valor:"))

print(f"O menor valor é {menor(n1, n2, n3)}")
