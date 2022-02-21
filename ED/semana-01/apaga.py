class BombaCombustivel:
    def __init__(self, nome):
        numero = 20
        self.frentista = nome
        self.preço_gasolina = 0
        self.preço_alcool = 0

    def teste(self):
        print('Teste',self.frentista)

# programa principal
b1 = BombaCombustivel('Alex')
b2 = BombaCombustivel('Ronaldo')
b1.teste()
b2.teste()
