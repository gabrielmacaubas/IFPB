class FilaException(Exception):
    pass

class Fila:
    def __init__(self, tamanho: int):
        self.__dados = [None] * tamanho
        self.__tamanho = tamanho
        self.__inicio = 0
        self.__quantidade = 0
        self.__posicao_livre = 0
    
    def esta_vazia(self):
        return self.obter_tamanho() == 0
    
    def esta_cheia(self):
        return (self.obter_quantidade() 
                == self.obter_tamanho())
    
    def obter_tamanho(self):
        return self.__tamanho

    def obter_quantidade(self):
        return self.__quantidade

    def enfileirar(self, dado):
        if self.esta_cheia():
            raise FilaException('fila cheia')

        self.__dados[self.__posicao_livre % self.__tamanho] = dado
        self.__quantidade += 1
        self.__posicao_livre += 1
    
    def desenfileirar(self):
        if self.esta_vazia():
            raise FilaException('fila vazia')
        
        dado =  self.__dados[self.__inicio]

        self.__quantidade -= 1
        self.__inicio += 1
        return dado

    def imprimir(self) -> str:
        for index in range(self.__inicio, self.__posicao_livre):
            print(f'{self.__dados[index % self.__tamanho]} ', end='')
        print()