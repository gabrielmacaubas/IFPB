class FilaException(Exception):
    pass


class No:

    def __init__(self, valor: int):
        self.valor: int = valor
        self.proximo = None


class Fila:

    def __init__(self):
        self.inicio: No = None
        self.fim: No = None
        self.tamanho: int = 0
    
    def esta_vazia(self):
        return self.inicio is None
    
    def obter_tamanho(self):
        return self.tamanho

    def enfileirar(self, valor: int):
        no = No(valor)

        if self.esta_vazia():
            self.inicio = no
        else:
            self.fim.proximo = no
        
        self.fim = no
        self.tamanho += 1

    def desenfileirar(self) -> int:
        if self.esta_vazia():
            raise FilaException('fila vazia')

        primeiro = self.inicio

        self.inicio = self.inicio.proximo
        self.tamanho -= 1

        return primeiro.valor

    def imprimir(self):
        no = self.inicio

        while no:
            print(f'{no.valor}, ', end='')
            no = no.proximo
            
        print()

