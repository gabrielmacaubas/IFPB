"""
Faça um programa que leia vários números, calcule e exiba a média desses
números.
Obs: a leitura do número 999 indica o fim dos dados de entrada e não deve ser
computado na média)
"""
print("Digite vários números (para encerrar, digite 999)")

numero = int()
soma = int()
contagem = int()
flag = 999

while numero != flag:
    numero = int(input())

    if numero != flag:
        soma += numero
        contagem += 1

print(f"Média = {(soma / contagem):.1f}")
