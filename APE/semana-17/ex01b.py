"""
Escreva também um programa que leia uma frase e, usando a função vogal
criada, imprima a quantidade de vogais existentes na frase lida.
"""
from ex01function import vogal

frase = str(input("Frase: "))

print(f"Vogais existentes na frase lida: {vogal(0, frase)}")
