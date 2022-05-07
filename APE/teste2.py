fumantes_jovens = int()
soma_idade = int()
numero_pessoas = 300
maior_idade = int()
menor_idade = int()

for i in range(numero_pessoas):
    idade = int(input(f"{i + 1}º pessoa Idade: "))
    fumante = input("Fumante (S/N): ").upper()

    if fumante == "S":
        if 20 >= idade <= 30:
            fumantes_jovens += 1

        if i == 0:
            maior_idade = idade
            menor_idade = idade

        else:
            if idade > maior_idade:
                maior_idade = idade

            elif idade < menor_idade:
                menor_idade = idade


    soma_idade += 1

print(fumantes_jovens)

media_idade = soma_idade / numero_pessoas
print(media_idade)

print(maior_idade)
print(menor_idade)
