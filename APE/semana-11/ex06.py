"""
O Brasil possui 26 estados e 1 distrito federal, totalizando 27 unidades
federativas. Escreva um programa para armazene, em um vetor, a sigla de todas
as unidades federativas. O programa deverá obter de vários usuários qual é a
unidade federativa ele acha mais interessante, informando a respectiva sigla. O
programa encerra quando for digitada uma sigla inexistente. Ao final, o
programa deverá exibir qual foi a sigla mais votada (considere possibilidade de
empate).
"""
uf = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RN", "RS", "RJ", "RO", "RR", "SC", "SP", "SE", "TO"]
n = len(uf)
cont = [0]*n

while True:
    voto = str(input("Digite a UF de sua preferência: "))
    for i in range(n):
        if uf[i] == voto:
            cont[i] += 1
            break

    else:
        break

maior = cont[0]
for number in range(n):
    if cont[number] > maior:
        maior = cont[number]

print('\nUF mais votada:')
for i in range(n):
    if cont[i] == maior:
        print(f'{uf[i]} com {maior} votos')
