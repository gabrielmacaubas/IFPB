class Carta:

        def __init__(self, numero, naipe, cor):
            self.numero = numero
            self.naipe = naipe
            self.cor = cor
        

        def getNaipe(self):
            return self.Naipe

        def mostrarCor(self):
            return self.cor

        def __str__(self): # todas as infromacoes da carta
            return f'{self.numero}'