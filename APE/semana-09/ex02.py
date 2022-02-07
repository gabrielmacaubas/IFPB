n = int(input("Digite o valor de N: "))

for numbers in range(1, n+1):
    cont_div = int()

    for c in range(1, numbers+1):

        if (numbers % c) == 0:
            cont_div += 1

    if cont_div == 2:
        print(numbers, end=' ')
