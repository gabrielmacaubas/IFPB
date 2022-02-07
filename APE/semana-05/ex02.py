
number_1 = int(input("numero 1: "))
number_2 = int(input("numero 2: "))
numeros = list()
temp = int()

numeros.append(number_1)
numeros.append(number_2)
numeros.sort()

print("Números sortidos ==> ", end='')

for n in numeros:
    if temp == 0:
        print(f"{n}, ", end=' ')
        temp = temp + 1

    else:
        print(f"{n}")

"""
number_1 = int(input("numero 1: "))
number_2 = int(input("numero 2: "))
if number_1 > number_2:
    print(number_2, number_1, sep=', ')
else:
    print(number_1, number_2, sep=', ')
"""
