def imc(x, y):
    return x / (y**2)


def grau(x):
    if x < 26:
        return "Normal"

    elif x < 30:
        return "Obeso"

    else:
        return "Obeso Mórbido"


nomes = list()
imcs = list()
graus = list()

while True:
    nome = str(input("\nDigite seu nome: "))
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite seu altura: "))

    i = imc(peso, altura)
    g = grau(i)

    nomes.append(nome)
    imcs.append(i)
    graus.append(g)

    continuar = str(input("\nVocê deseja enviar mais dados(S/N)? ")).upper()
    if continuar == "N" or continuar != "S":
        break

for i in range(len(nomes)):
    print(f"\nNome --> {nomes[i]}\nIMC --> {imcs[i]:.2f}\nGrau de obesidade --> {graus[i]}\n")
