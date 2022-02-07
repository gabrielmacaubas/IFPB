n = int(input('Digite o número de termos desejado: '))
n2 = 1
n1 = 0
soma = int()

print("Sequência de Fibonacci:", n1, n2, end=' ')

for c in range(n-2):
    soma = n2 + n1
    n2 = soma
    n1 = n2
    print(soma, end=' ')
