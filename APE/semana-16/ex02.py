"""
Escreva uma função chamada fatorial que receba um número inteiro e retorne
seu fatorial. Faça também um programa para testar a função.
"""


def fatorial(x):
    resultado = 1
    for i in range(1, x+1):
        resultado = resultado * i

    print(f"{x}! = {resultado}")


n = int(input("Digite um valor para o cálculo do seu fatorial: "))
fatorial(n)
