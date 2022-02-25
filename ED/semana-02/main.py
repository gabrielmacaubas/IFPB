from Bomba import *

# programa principal
b1 = BombaDeCombustivel(6.50, 5.20)
print(b1.preço_gasolina)
print(b1.__dict__)
b1.preço_gasolina = 6.10
print(b1.__dict__)

b1.zerarBomba(BombaDeCombustivel.GASOLINA)

b1.desligar()
if b1.ligada == False:
    print('****** A bomba foi desligada neste momento ******')

visor_alcool = Visor(5.20, 'ALCOOL')
print(visor_alcool)

visor_gasolina = Visor(5.20, 'GASOLINA')
print(visor_gasolina)
