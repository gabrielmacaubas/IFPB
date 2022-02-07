"""
Escreva um programa que leia as 3 notas de um aluno, determine e exiba a sua
média e seu conceito.
O programa deve conter as seguintes funções:
• Uma função que recebe como parâmetros as 3 notas do aluno e retorne a sua
média (aritmética).
• Uma função que receba como parâmetro a média do aluno e retorne o seu
conceito, de acordo com a tabela abaixo:

    MÉDIA          CONCEITO
    >= 8,0            A
  >= 5,0 e < 8,0      B
    < 5,0             C
"""


def media(x, y, z):
    return (x + y + z) / 3


def conceito(x):
    if x >= 8:
        return "A"

    elif x >= 5:
        return "B"

    else:
        return "C"


print("Informe 3 notas")
n1 = int(input("1ª nota:"))
n2 = int(input("2ª nota:"))
n3 = int(input("3ª nota:"))

media = media(n1, n2, n3)
print(f"\nA média é: {media:.1f}")
print(f"O conceito é: {conceito(media)}")
