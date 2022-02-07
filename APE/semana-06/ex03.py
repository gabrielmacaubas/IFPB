ano = int(input("digite um ano: "))
ano_tipo = str()

if ((ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0)):
    ano_tipo = "bissexto"

else:
    ano_tipo = "Nao bissexto"

print(ano_tipo)
