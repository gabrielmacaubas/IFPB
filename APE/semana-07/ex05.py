"""
Faça um programa que, para um grupo de N pessoas (obs: N será lido):
• Leia o sexo (M ou F) de cada pessoa;
• Calcule e escreva o percentual de homens;
• Calcule e escreva o percentual de mulheres.
"""

n = int(input("grupo de quantas pessoas: "))
mulheres = int()
homens = int()

for p in range(1, n+1):
    sexo = str(input("sexo (M ou F): "))

    if sexo == "F" or sexo == "f":
        mulheres += 1

    elif sexo == "M" or sexo == "m":
        homens += 1

mulheres_porcento = (100 * mulheres) / n
homens_porcento = (100 * homens) / n

print(f'Percentual de homens: {homens_porcento:.1f}%\nPercentual de mulheres: {mulheres_porcento:.1f}%')
