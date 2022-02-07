"""
Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele
próprio. Faça um programa que leia um número e determine se ele é ou não
primo.
"""

numero = int(input("Digite um numero: "))
divisoes = int()

for n in range (1, numero + 1):

    if numero % n == 0:
        divisoes += 1

if divisoes == 2:
    print("numero primo")

else:
    print("numero nao primo")
