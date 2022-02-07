"""
Faça um programa que calcule e mostre os números múltiplos de 5 do
intervalo 50 a 300, juntamente com suas raízes e seus cubos.
"""
import math

for n in range(50, 301):

    if n % 5 == 0:
        print(f'{n:^10} {math.sqrt(n):^10.2f} {n**3:^10}')
