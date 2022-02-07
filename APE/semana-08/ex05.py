"""
Faça um programa que leia um número inteiro e determine se ele é par ou
ímpar. Ao final, o programa deve perguntar se o usuário deseja continuar
(digitar outro número) ou sair. Se o usuário quiser continuar, o programa deve
repetir tudo de novo, caso contrário o programa deve ser encerrado.
"""
resposta = "s"
tipo = str()

while resposta == "s":
    numero = int(input("Digite um número inteiro: "))

    if numero % 2 == 0:
        tipo = "par"

    else:
        tipo = "ímpar"

    print(f"{numero} é {tipo}")

    resposta = str(input("Deseja Continuar (S/N)? ")).lower()

    print()

print("Fim do programa")
