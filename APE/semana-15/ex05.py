"""
Faça um programa que leia uma frase e a exiba na tela conforme o exemplo
abaixo.

Exemplo:

    Entrada: ABCDE

    Saída:  A
            BB
            CCC
            DDDD
            EEEEEE
            DDDD
            CCC
            BB
            A
"""
print("Frase:")

frase = str(input())

print("\nSaída")

for i in range(len(frase) + 1):
    print(frase[i - 1]*i)

for i in range(len(frase) - 1, 0, -1):
    print(frase[i - 1]*i)
