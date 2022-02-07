"""
Faça um programa que calcule e mostre o fatorial de um número N, fornecido
pelo usuário. A definição de fatorial é mostrada a seguir:
"""
numero = int(input("Entre com um número inteiro: "))
resultado = 1

for elemento in range(1, numero + 1):
    resultado = resultado * elemento

print(f"{numero}! = {resultado}")
