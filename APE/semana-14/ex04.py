"""
Faça um programa que leia uma frase e a exiba com a inicial de cada palavra em
maiúsculo.
"""
frase = str(input("Frase: "))
divisao = frase.split()
for p in divisao:
    print(p.capitalize(), end=" ")

