nota_1 = float(input("Primeira prova: "))
nota_2 = float(input("Segunda prova: "))
media = (nota_1 + nota_2) / 2
situacao = str()

if media >= 7.0:
    situacao = "\nApto para segunda etapa.\n"

    print(situacao)

    nota_3 = float(input("Terceira prova: "))

    if nota_3 >= 8.0:
        situacao = "\nAprovado no Concurso.\n"

        print(situacao)

    else:
        situacao = "\nNao aprovado no Concurso.\n"

        print(situacao)

else:
    situacao = "\nNao aprovado no Concurso.\n"

    print(situacao)
