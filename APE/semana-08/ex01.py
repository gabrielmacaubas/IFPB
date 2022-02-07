"""
Faça um programa que leia 30 números inteiros, calcule e mostre a soma deles
Obs: não use o comando for, use while.
"""
contador = int()
soma = int()

print("Digite 30 números inteiro:")

while contador < 30:
    numero = int(input())
    soma += numero
    contador += 1

print(soma)
