class FilaException(Exception):
    pass

class No:

    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
    

class Fila:

    def __init__(self):
        self.inicio = None
    
    def esta_vazia(self):
        return self.inicio is None
    
    def obter_tamanho(self): ...

    def enfileirar(self, valor): ...

    def desenfileirar(self): ...

    