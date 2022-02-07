hodometro_antes = int(input("Hodômetro do veículo antes da viagem:"))
hodometro_depois = int(input("Hodômetro do veículo depois da viagem:"))
combustivel_gasto = int(input("Litros de combustível gastos: "))
preco_combustivel = int(input("Preço do litro do combustível: "))
capacidade_tanque = int(input("Capacidade do tanque: "))
kilometros = hodometro_depois - hodometro_antes
consumo = kilometros / combustivel_gasto

print(kilometros)
print(consumo)
print(capacidade_tanque *  consumo)
print(combustivel_gasto / preco_combustivel)
