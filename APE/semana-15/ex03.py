"""
Faça um programa que leia o nome de uma pessoa e exiba-o conforme o exemplo
abaixo.
Obs: Suponha que o nome lido não possua nenhuma preposição, artigo, etc.
Exemplo:
Entrada: FLAVIO RIBEIRO COUTINHO
Saída: COUTINHO, F. R.
"""
nome = str(input("Nome:\n")).upper().split()

print(f"{nome[-1]}, ", end="")

for i in range(len(nome) - 1):
    print(f"{nome[i][0]}. ", end="")
