"""
O cardápio de uma casa de lanches, especializada em sanduíches, é dado a
seguir.
    CÓDIGO NOME          PREÇO
    H      Hamburger     R$ 5,00
    C      Cheese Burger R$ 6,00
    B      Cheese Bacon  R$ 7,00
    F      Cheese Frango R$ 4,00

Faça um programa que leia o código e a quantidade de cada item comprado
por um cliente (a leitura do código “X” indica o fim dos dados de entrada). Ao
final, calcule e exiba o total a pagar.
Veja o exemplo abaixo, considerando que o cliente pediu 3 Hamburger e 2
Cheese Bacon:
Entrada:
    Código: H
    Quantidade: 3
    Código: B
    Quantidade: 2
    Código: X
Saída:
    Total a pagar: R$ 29.00
"""
print(f'Informe o código e a quantidade dos itens.\nPara encerrar, digite o código "X"')

codigo = str(input("Código: ")).upper()
flag = "X"
total = float()

while codigo != flag:
    quantidade = int(input("Quantidade: "))

    if codigo == "F":
        total += (4 * quantidade)

    elif codigo == "H":
        total += (5 * quantidade)

    elif codigo == "C":
        total += (6 * quantidade)

    elif codigo == "B":
        total += (7 * quantidade)

    codigo = str(input("\nCódigo: ")).upper()

print(f"\nTotal a pagar: R$ {total:.2f}")
