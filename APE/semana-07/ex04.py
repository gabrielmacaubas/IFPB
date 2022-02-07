"""
Faça um programa que leia 20 números inteiros, determine e mostre o maior
deles.
"""

maior_numero = 0

print("-- 20 numeros inteiros deverao ser inseridos --")

for c in range(1, 21):
    numero = int(input("Digite um numero inteiro: "))

    if numero >= maior_numero:
        maior_numero = numero

print(maior_numero)
