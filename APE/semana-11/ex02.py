"""
Dados dois vetores A e B contendo N elementos inteiros cada (N, A e B serão
lidos), gerar e exibir um vetor C (de tamanho N*2) cujos elementos sejam a
intercalação dos elementos de A e B.
Ex: N = 3, A = [18, 12, 20], B = [15, 10, 7], C = [18, 15, 12, 10, 20, 7]
"""
n = int(input("Digite o valor de N: "))
a = [None] * n
b = [None] * n
c = [None] * (n * 2)
cont = int()

print("\nDigite os elementos do vetor A:")

for number in range(n):
    a[number] = int(input(f"A[{number}]: "))

for number in range(len(c)):
    if number % 2 == 0:
        c[number] = a[cont]
        cont += 1


print("\nDigite os elementos do vetor B:")

for number in range(n):
    b[number] = int(input(f"B[{number}]: "))

cont = 0

for number in range(len(c)):
    if number % 2 != 0:
        c[number] = b[cont]
        cont += 1

print(f"\nA =  {a}")
print(f"B =  {b}")
print(f"C =  {c}")
