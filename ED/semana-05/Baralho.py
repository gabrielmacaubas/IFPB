# Baralho = coleção de cartas (lista de cartas)

class BaralhoException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


from Carta import Carta


class Baralho:
    def __init__(self):
        self.baralho = list()
        naipe = ["Ouro", "Espada", "Paus", "Copas"]
        cor = ["vermelho", "preto", "preto", "vermelho"]
        numeracao = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "valete", "dama", "rei"]

        for idx in range(len(naipe)):
            for id in numeracao:
                self.baralho.append(Carta(id, naipe[idx], cor[idx]))

    def __len__(self):
        return len(self.baralho)

    def temCarta(self):
        if len(self.baralho) > 0:
            return True
        else:
            return False

    def retirarCarta(self) -> Carta:
        try:
            return self.baralho.pop()
        except IndexError:
            raise BaralhoException('O baralho está vazio. Não há cartas para retirar')

    def numCartas(self):
        return len(self.baralho)

    def __str__(self):
        saida = ''
        for carta in self.baralho:
            saida += carta.__str__() + '\n'
        return saida
