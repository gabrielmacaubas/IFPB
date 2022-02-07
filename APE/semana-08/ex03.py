"""
Faça um programa que leia vários números, determine e mostre o maior e o
menor deles.
Obs: a leitura do número 0 (zero) encerra o programa.
"""
print("Digite vários números (para encerrar, digite 0)")

numero = int(input())
maior = numero
menor = numero
flag = 0

while numero != flag:
    numero = int(input())

    if numero != flag:
        if numero > maior:
            maior = numero

        elif numero < menor:
            menor = numero

print(f"Maior = {maior}\nMenor = {menor}")
