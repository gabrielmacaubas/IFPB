"""
Escreva um programa para ler 6 números. Após a leitura dos números, verifique,
para cada um deles, se é distinto, ou seja, não possui repetição.
"""
numeros = [None] * 6

for numero in range(6):
    numeros[numero] = int(input(f"{numero + 1}º número: "))

print()

for numero in numeros:

    repeticoes = int()
    repete = False

    for c in range(6):
        if numero == numeros[c]:
            repeticoes += 1

    if repeticoes > 1:
        repete = True

    if repete:
        print(f"{numero} repete")

    else:
        print(f"{numero} não repete")
