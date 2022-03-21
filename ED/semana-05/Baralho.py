# Baralho = coleção de cartas (lista de cartas)
from Carta import Carta
class Baralho:
    def __init__(self):
        self.baralho = list()
        naipe = ["Ouro",     "Espada","Paus","Copas"]
        cor =   ["vermelho", "preto","preto","vermelho"]
        numeracao = ["As","1","2","3","4","5","6","7","8","9","10","valete","dama","rei"]

        for idx in range(naipe):
            for id in numeracao:
                self.baralho.append( Carta(id, naipe[idx], cor[idx]))
    
    def numCartas(self):
        return len(self.baralho)
    
    def __str__(self):
        saida = ''
        for carta in self.baralho:
            saida += carta
        return saida
