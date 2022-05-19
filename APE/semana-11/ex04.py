"""
Escreva um programa para ler 6 números distintos, ou seja, não podem repetir.
Exiba os números lidos.
"""
print("Digite 6 números distintos")

numeros = [None] * 6
numeros[0] = int(input())

for numero in range(1, 6):
    while True:
        repeticoes = int()
        numeros[numero] = int(input())

        for c in range(0, numero):

            if numeros[numero] == numeros[c]:
                repeticoes += 1
                print("Número já existente. Digite novamente")

        if repeticoes == 0:
            break

print(f"\nNúmeros válidos: {numeros}")
