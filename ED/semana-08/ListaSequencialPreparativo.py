class ListaSequencial:

    def __init__(self):
        self.__dados = []
    
    def vazia(self):
        return len(self.__dados) == 0
    

#    def cheia(self):
#        pass

    def tamanho(self):
        return len(self.__dados)

    def busca(self, dado):
        for i in range(self.__dados):
            if self.__dados[i] == dado:
                return i+1



    # operacao que recebe a posicao de um elemento da lista e retorna
    # o conteúdo (dado) que está armazenado
    def elemento(self, posicao):
        return self.__dados[posicao-1]

    # função que insere um dado na lista na posicao indicada (posição válida)
    def inserir(self, posicao, dado):
        self.__dados.insert(posicao-1, dado)

    # operação que remove um elemento da lista e retorna seu valor
    def remover(self, posicao):
        if( self.vazia()):
            return None
        valor = self.__dados[posicao-1]
        del self.__dados[posicao-1]
        return valor

    # método especial que retorna a descrição interna do objeto
    def __str__(self):
        return self.__dados.__str__()
    
    # método que imprime o conteúdo da Lista Sequencial
    def imprimir(self):
        print(self.__str__())

    # método que altera o conteúdo armazenado em uma determinada posição da lista
    def modificar(self, posicao, novoValor):
        if( self.vazia()):
            return False
        self.__dados[posicao-1] = novoValor
        return True


# testando se a Lista Sequencial está atuando como um módulo (biblioteca) ou se o 
if (__name__ == '__main__'):
    print('Rodando o programa principal a partir da classe ListaSequencial')
    l1 = ListaSequencial()
    if (l1.vazia()):
        print('Lista está vazia')
    
    print('Tamanho: ', l1.tamanho())

    for i in range(10):
        l1.inserir(1,i*10)
        print(l1)

    valor = l1.remover(2)
    print(valor)
    print(l1)

    print()
    l1.imprimir()
    l1.modificar(5,44)
    l1.imprimir()

    l1.inserir(-10,99)
    print(l1)



