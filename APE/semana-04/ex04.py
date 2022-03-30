"""
Um motorista anota a marcação do hodômetro do seu veículo antes e após uma viagem,
bem como o número de litros de combustível gastos.
Escreva um programa que leia os 3 dados acima, o preço do litro de combustível, a
capacidade do tanque e mostre:
a) Quilometragem rodada.
b) Quantos quilômetros por litro faz o veículo.
c) Autonomia do veículo.
d) Custo da viagem.
"""

quilometragem_antes = int(input("Odômetro inicial (Km): "))
quilometragem_depois = int(input("Odômetro final (Km): "))
combustivel_gasto = int(input("Quantidade gasta de combustível (litros): "))

preco_combustivel = int(input("Preço do litro do combustível (R$): "))
capacidade_tanque = int(input("Capacidade do tanque (litros): "))


# a
quilometros_rodados = quilometragem_depois - quilometragem_antes
print(f"\nQuilometragem rodada: {quilometros_rodados} km")


# b
consumo = quilometros_rodados / combustivel_gasto
print(f"Consumo: {consumo:.1f} km/L")


# c
autonomia = capacidade_tanque * consumo
print(f"Autonomia: {autonomia:.0f} km")


# d
custo = combustivel_gasto * preco_combustivel
print(f"Custo da viagem: R$ {custo:.1f}")
