numero = int(input("Digite um numero de 1 a 7 correspondente a um dia da semana: "))
dia = str()
dia_tipo = str()

if 1 < numero < 7:
    dia_tipo = "dia util"

    if numero == 2:
        dia = "Segunda"

    elif numero == 3:
        dia = "Terca"

    elif numero == 4:
        dia = "Quarta"

    elif numero == 5:
        dia = "Quinta"

    elif numero == 6:
        dia = "Sexta"

else:
    dia_tipo = "final de semana"

    if numero == 1:
        dia = "Domingo"

    elif numero == 7:
        dia = "Sabado"

print(dia, dia_tipo, sep=", ")
