"""
Escreva um programa que:
• Crie uma matriz de ordem 20 x 4 e armazene nela as 3 notas dos 20 alunos de uma
turma e a média de cada um deles.
o As notas serão lidas e armazenadas nas 3 primeiras colunas da matriz;
o As médias serão calculadas e armazenadas na 4a coluna da matriz.
• Imprima as notas dos alunos e suas respectivas médias (no formato de matriz).
• Calcule e imprima a média geral da turma.
• Calcule e imprima o número de alunos com média superior à média geral da turma.
"""
print("Digita as notas dos alunos")

alunos = 2
notas = 3
matriz = [[None] * (notas + 1) for i in range(alunos)]
medias_soma = int()

for a in range(alunos):
    soma = int()

    print(f"\n{a + 1}º ALUNO:")

    for n in range(notas):
        matriz[a][n] = int(input(f"{n + 1}ª Nota: "))
        soma += matriz[a][n]

    matriz[a][notas] = soma / notas
    medias_soma += matriz[a][notas]

print(f"\n{'1ª NOTA':>17}{'2ª NOTA':>9}{'3ª NOTA':>9}{'MÉDIA':>9}")


for a in range(alunos):
    print(f"{a + 1}º ALUNO", end="")

    for n in range(notas + 1):
        print(f"{matriz[a][n]:>9.1f}", end="")

    print()

media_turma = medias_soma / len(matriz)

print(f"\nMédia geral da turma: {media_turma:.1f}")

alunos_adm = int()

for a in range(alunos):
    for n in range(notas, notas - 1, -1):

        if matriz[a][n] > media_turma:
            alunos_adm += 1

print(f"\nNúmero de alunos com média superior à média geral da turma: {alunos_adm}")
print(matriz)