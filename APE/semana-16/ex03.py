"""
Escreva uma função chamada vertical que receba como parâmetro uma string e
a exiba na vertical, ou seja, com uma letra em cada linha. Faça também um
programa para testar a função.
"""


def vertical(x):
    print("\nSaída:")
    for c in x:
        print(c)


print("Digite uma frase:")
f = str(input())
vertical(f)
