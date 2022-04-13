class ListaException(Exception):
    pass


class No:

    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class Lista:
    def __init__(self):
        self.__inicio = None
        self.__tamanho = 0

    def esta_vazia(self):
        return self.__inicio is None
    
    def obter_tamanho(self):
        return self.__tamanho
    
    def insereNoInicio(self, valor):
        no = No(valor)
        if self.esta_vazia():
            self.__inicio = no
        else:
            inicio = self.__inicio
            self.__inicio = no
            no.proximo = inicio
        self.__tamanho += 1
    
    def insereNoFim(self, valor):
        novo_elemento = No(valor)
        if self.esta_vazia():
            self.__inicio = novo_elemento
        else:
            elemento = self.__inicio
            while elemento.proximo:
                elemento = elemento.proximo
            elemento.proximo = novo_elemento
        self.__tamanho += 1

    def obter_elemento(self, indice : int):
        if self.esta_vazia():
            raise ListaException("lista vazia")
        if not (0 <= indice < self.obter_tamanho()):
            raise ListaException("Erro de índice")
        no = self.__inicio
        atual = 0
        while no:
            if indice == atual:
                return no.valor
            no = no.proximo
            atual += 1

    def removerDoInicio(self):
        if self.esta_vazia():
            raise 

        self.__inicio = self.__inicio.proximo
        self.__tamanho -= 1

    def inserir(self, posicao, valor):
        indice = 0
        no = self.__inicio
        while indice != posicao - 1:
            no = no.proximo
            indice += 1
        
        novo_no = No(valor)
        proximo = no.proximo
        no.proximo = novo_no
        novo_no.proximo = proximo

        self.__tamanho += 1
    
    def remover(self, posicao):
        if self.esta_vazia():
            raise ListaException("lista vazia")
        if not (0 <= posicao < self.obter_tamanho()):
            raise ListaException("Erro de índice")
        
        if self.obter_tamanho() == 1:
            self.__inicio = None
        else:
            indice = 0
            no = self.__inicio
            while indice != posicao - 1:
                no = no.proximo
                indice += 1
            
            no.proximo = no.proximo.proximo
            self.__tamanho -= 1

    def imprimir(self):
        no = self.__inicio
        while no:
            print(f'{no.valor} -> ', end='')
            no = no.proximo
        print()
