vendas = [
    [204, 323, 230, 257, 290, 222],
    [295, 192, 198, 203, 308, 228],
    [220, 222, 317, 231, 245, 280],
    [254, 262, 279, 284, 296, 230]
]

fabricantes = ["Chevrolet", "Fiat", "Ford", "Volkswagen"]
anos = [2013, 2014, 2015, 2016, 2017, 2018]
ano_maior_vendas = [int(), int()]

print(f"Fabricante/Ano", end=" ")

for a in anos:
    print(f"{a:5}", end=" ")

print()

for l in range(4):
    print(f"{fabricantes[l]:^15}", end=" ")

    for c in range(6):
        print(f"{vendas[l][c]:<5}", end=" ")

    print()

print("-" * 60)
print("\nFabricante com maiores vendas em cada ano -->\n")

for i in range(6):
    nome_fabricante = str()
    vendas_fabricante = int()
    ano_fabricante = int()
    soma_vendas_vertical = int()

    for l in range(4):
        soma_vendas_vertical += vendas[l][i]

        if vendas[l][i] > vendas_fabricante:

            vendas_fabricante = vendas[l][i]
            nome_fabricante = fabricantes[l]
            ano_fabricante = anos[i]

    print(f"{ano_fabricante}: {nome_fabricante} com {vendas_fabricante} vendas.")

    if soma_vendas_vertical > ano_maior_vendas[1]:
        ano_maior_vendas[1] = soma_vendas_vertical
        ano_maior_vendas[0] = anos[i]

print("-" * 60)
print(f"\nAno onde houve o maior volume de vendas -->")
print(f"\nEm {ano_maior_vendas[0]} houveram {ano_maior_vendas[1]} vendas.")
print("-" * 60)
print(f"\nMédia de vendas de cada fabricante entre 2013 e 2018 -->\n")

for l in range(4):
    soma_vendas_horizontal = int()

    for c in range(6):
        soma_vendas_horizontal += vendas[l][c]

    print(f"{fabricantes[l]}: {(soma_vendas_horizontal / len(anos)):.2f}")
