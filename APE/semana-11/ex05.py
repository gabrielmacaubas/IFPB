"""
Faça um programa para ler as 8 dezenas apostadas por 20 apostadores e
verificar se a aposta é válida (cada dezena está entre [1, 80] e não pode haver
repetição). O programa deverá calcular e exibir a quantidade de números
acertados em cada aposta.
Atenção! As dezenas sorteadas são: 06, 07, 13, 14 e 26.
"""
apostador = [None] * 8
dezenas = [6, 7, 13, 14, 26]

for p in range(3):
    print(f"\nDezenas do Apostador {p + 1}:")

    for n in range(8):
        apostador[n] = int(input())

    validade = True
    acertos = int()

    for num in apostador:
        repeticoes = int()

        if 1 <= num <= 80:
            for d in dezenas:
                if num == d:
                    acertos += 1

            for o in range(0, 8):
                if num == apostador[o]:
                    repeticoes += 1

            if repeticoes > 1:
                validade = False

        else:
            validade = False

    if not validade:
        print("Aposta inválida")

    else:
        print(f"Número de acertos: {acertos}")
