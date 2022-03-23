from Baralho import Baralho, BaralhoException

baralho = Baralho()
print(baralho.numCartas())
print(baralho)
print(len(baralho))

print('\nRetirando as cartas')
while(True):
    try:
        c = baralho.retirarCarta()
        print('Carta:', c, ' Baralho: ', len(baralho))
        print('Todas as cartas do baralho foram retiradas')
    except BaralhoException as be:
        print('Fim! todas as cartas foram retiradas')
        break