# PEP-8
# pilha_sequencial.py

class PilhaException(Exception):
    pass

class Pilha:

    def __init__(self, tamanho: int):
        self.__quantidade = 0
        self.__tamanho = tamanho
        self.__dados = [None] * tamanho

    def empilha(self, dado):
        try:
            self.__dados[self.__quantidade] = dado
            self.__quantidade += 1
        except IndexError:
            raise PilhaException("pilha cheia")
    
    def desempilha(self):
        if self.estah_vazia():
            raise PilhaException("pilha vazia")

        valor = self.__dados[self.__quantidade - 1]
        self.__quantidade -= 1
        print(self.__dados)
        return valor
        

    def obter_tamanho(self):
        return self.__tamanho

    def obter_quantidade(self):
        return self.__quantidade

    def estah_vazia(self):
        return self.obter_quantidade() == 0

    def estah_cheia(self):
        return self.obter_quantidade() == self.__tamanho

