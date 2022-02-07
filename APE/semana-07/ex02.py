"""
Faça um programa que leia um número N, inteiro, e some todos os números
de 1 até N, mostrando o resultado.
"""
n = int(input("Numero: "))
resultado = int()

for numero in range(1, n+1):
    resultado = resultado + numero

print(resultado)
