"""
Chico tem 1,50 metros e cresce 2 centímetros por ano, enquanto Zé tem 1,10
metros e cresce 3 centímetros por ano. Faça um programa que calcule e
imprima quantos anos serão necessários para que Zé seja maior que Chico.
"""
chico_altura = 1.50
ze_altura = 1.10
tempo = int()

while chico_altura > ze_altura:
    chico_altura += 0.02
    ze_altura += 0.03
    tempo += 1

print(f"Serão necessários {tempo} anos para que Zé seja maior que Chico")
