"""
Escreva um programa que receba um vetor V de N números inteiros (N será lido),
determine e exiba o maior e o menor elemento deste vetor e seus respectivos
índices.
Obs: suponha a inexistência de valores repetidos.
"""
v_tamanho = int(input("Digite o tamanho do vetor: "))
v = [None] * v_tamanho
primeira_contagem = True

print(f"Digite os {v_tamanho} elementos do vetor:")

for elemento in range(v_tamanho):
    v[elemento] = int(input())

    if primeira_contagem:
        maior = v[elemento]
        menor = v[elemento]
        primeira_contagem = False

    elif v[elemento] > maior:
        maior = v[elemento]
        indice_maior = elemento

    elif v[elemento] < menor:
        menor = v[elemento]
        indice_menor = elemento

print(f"\nVetor = {v}")
print(f"\nMaior = {maior}\nIndice = {indice_maior}")
print(f"\nMenor = {menor}\nIndice = {indice_menor}")
