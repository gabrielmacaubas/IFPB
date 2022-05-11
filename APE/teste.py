# Lendo-se os números
number_1 = int(input("Digite o 1º número: "))
number_2 = int(input("digite o 2º número: "))
number_3 = int(input("digite o 3º número: "))
number_4 = int(input("digite o 4º número: "))

# Cálculo da soma
soma = number_1 + number_2 + number_3 + number_4
media = int()

# Cálculo da média
if number_1 <= number_2 and number_1 <= number_3 and number_1 <= number_4:
    soma -= number_1
    media = soma / 3

elif number_2 <= number_3 and number_2 <= number_1 and number_2 <= number_4:
    soma -= number_2
    media = soma / 3

elif number_3 <= number_1 and number_3 <= number_2 and number_3 <= number_4:
    soma -= number_3
    media = soma / 3

else:
    soma -= number_4
    media = soma / 3

# Determinação do conceito
conceito = str()
aprovacao = "APROVADO"

print(media)

if media >= 9:
    conceito = "A"

elif media >= 8:
    conceito = "B"

elif media >= 6:
    conceito = "C"

elif media >= 4:
    conceito = "D"
    aprovacao = "REPROVADO"

else:
    conceito = "E"
    aprovacao = "REPROVADO"

print(media, conceito, aprovacao)
