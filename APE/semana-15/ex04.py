"""
Faça um programa que leia uma string S e um valor inteiro N, e exiba na tela a
string S com as suas vogais repetidas N vezes.
Exemplo:
Entrada: S: Hoje tem aula de Python

N: 3

Saída: Hooojeee teeem aaauuulaaa deee Pythooon
"""
print("Digite uma frase:")

s = str(input())

print("\nDigite um valor inteiro:")

n = int(input())
vogais = "aAeEiIoOuU"
novo_s = str()

for c in s:
    if c in vogais:
        novo_s += c * n

    else:
        novo_s += c

print("Saída: ")
print(novo_s)
