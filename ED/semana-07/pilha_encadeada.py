class PilhaException(Exception):
    pass
    
class No:

    def __init__(self, valor: int):
        self.valor : int = valor
        self.proximo = None

class Pilha:

    def __init__(self):
        self.topo : No = None
        self.tamanho: int = 0
    
    def esta_vazia(self):
        return self.topo is None
    
    def obter_tamanho(self):
        return self.tamanho

    def empilhar(self, valor: int):
        no = No(valor)
        if self.esta_vazia():
            self.topo = no
        else:
            topo_atual = self.topo
            no.proximo = topo_atual
            self.topo = no

        self.tamanho += 1

    def desempilhar(self) -> int:
        if self.esta_vazia():
            raise PilhaException('fila vazia')

        topo = self.topo
        self.topo = topo.proximo
        self.tamanho -= 1
        return topo.valor

    def imprimir(self):
        no = self.topo
        while no:
            print(f'{no.valor}, ', end='')
            no = no.proximo
        print()

