class ListaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Node:
    def __init__(self, dado):
        self.__dado = dado
        self.__prox = None

    @property
    def dado(self):
        return self.__dado

    @property
    def prox(self):
        return self.__prox

    @dado.setter
    def dado(self, novoDado):
        self.__dado = novoDado

    @prox.setter
    def prox(self, novoProx):
        self.__prox = novoProx
    
    def __str__(self):
        return str(self.__dado)



class Lista:

    def __init__(self):
        self.__head = None
        self.__tamanho = 0
    
    def vazia(self):
        return True if self.__tamanho == 0 else False
    

#    def cheia(self):
#        pass

    def tamanho(self):
        return self.__tamanho

    def busca(self, dado):
        if( self.vazia()):
            raise ListaException('A lista está vazia')

        cursor = self.__head
        contador = 1

        while( cursor != None):
            if( cursor.dado == valor):
                return contador
            
            cursor = cursor.prox
            contador += 1

        raise ListaException('O valor informado na busca não está naa lista')

    # operacao que recebe a posicao de um elemento da lista e retorna
    # o conteúdo (dado) que está armazenado
    def elemento(self, posicao):
        # valor negativo?
        # posicao invalida IndexError
        # posicao com o tipo de dado diferente de int TypeError
        try:
            assert posicao > 0

            if( self.vazia()):
                raise ListaException('Lista está vazia')

            cursor = self.__head
            contador = 1    

            while( (cursor !=None) and (contador < posicao)):
                cursor = cursor.prox
                contador += 1
            
            if( cursor != None):
                return cursor.dado

            raise ListaException('A posicao é invalida para a lista')
        except TypeError:
            raise ListaException('O argumento posicao deve ser um valor do tipo inteiro')
        except AssertionError:
            raise ListaException('Posicao negativa não é válida para a lista')
        except:
            raise

    # função que insere um dado na lista na posicao indicada (posição válida)
    def inserir(self, posicao, dado):
        try:
            assert posicao > 0
            # CONDICAO 1: insercao se a lista estiver vazia

            if( self.vazia()):
                if( posicao != 1):
                    raise ListaException('A lista esta vazia. Defina o argumento posicao como 1')
                self.__head = Node(dado)
                self.__tamanho += 1
                return

            #CONDICAO 2: insercao na primeira posicao em uma lista nao vazia
            if( posicao == 1):
                novo = Node(dado)
                novo.prox = novo
                self.__head = novo
                self.__tamanho += 1
                return
            
            #CONDICAO 3: insercao apos a primeira posicao em uma lista nao vazia
            cursor = self.__head
            contador = 1
            while( (contador < posicao-1) and (cursor != None)):
                cursor = cursor.prox
                contador += 1
            
            if( cursor == None):
                raise ListaException('A posicao é invalida para insercao')
            
            novo = Node(dado)
            novo.prox = cursor.prox
            cursor.prox = novo
            self.__tamanho += 1

        except TypeError:
            raise ListaException('O argumento posicao deve ser um valor do tipo inteiro')
        except AssertionError:
            raise ListaException('Posicao negativa não é válida para a lista')
        except:
            raise

    # operação que remove um elemento da lista e retorna seu valor
    def remover(self, posicao):
        try:
            assert posicao > 0
            if( self.vazia()):
                raise ListaException('Lista Vazia. Não é possível remover elementos')

            cursor = self.__head
            contador = 1

            while((contador <= posicao-1) and (cursor !=None)):
                anterior = cursor
                cursor = cursor.prox
                contado += 1
            
            if( cursor == None):
                raise ListaException('Posicao invalida para remoção')

            dado = cursor.dado

            if( posicao == 1):
                self.__head = cursor.prox
            else:
                anterior.prox = cursor.prox
            
            self.__tamanho -= 1
            return dado
        except TypeError:
            raise ListaException('O argumento posicao deve ser um valor do tipo inteiro')
        except AssertionError:
            raise ListaException('Posicao negativa não é válida para a lista')
        except:
            raise

    # método especial que retorna a descrição interna do objeto
    def __str__(self):
        str  = 'Lista: [ '
        cursor = self.__head
        while( cursor != None):
            str += f'{cursor.dado}'
            cursor = cursor.prox
            if( cursor != None):
                str += ', '
        str += ']'
        return str
    
    # método que imprime o conteúdo da Lista Sequencial
    def imprimir(self):
        print(self.__str__())

    # método que altera o conteúdo armazenado em uma determinada posição da lista
    def modificar(self, posicao, novoValor):
        try:
            assert posicao > 0
            if( self.vazia()):
                raise ListaException('Lista Vazia. Não é possível remover elementos')

            cursor = self.__head
            contador = 1

            while( cursor!= None) and (contador < posicao)):
                cursor = cursor.prox
                contador += 1
            
            if( cursor != None):
                cursor.dado = novoValor
                return

            raise ListaException('Posicao invalida para a lista')

        except TypeError:
            raise ListaException('O argumento posicao deve ser um valor do tipo inteiro')
        except AssertionError:
            raise ListaException('Posicao negativa não é válida para a lista')
        except:
            raise


# testando se a Lista Sequencial está atuando como um módulo (biblioteca) ou se o 
if (__name__ == '__main__'):
    print('Rodando o programa principal a partir da classe ListaSequencial')


    l1 = Lista()

    if (l1.vazia()):
        print('Lista está vazia')
    
    print('Tamanho: ', l1.tamanho())

    for i in range(10):
        l1.inserir(1,i*10)
    print(l1)

    l1.inserir(1,999)
    print(l1)

    l1.inserir(5,888)
    print(l1)

    l1.inserir(5,111)
    print(l1)
    
    try:
        l1.inserir(15,333)
        print(l1)
    except ListaException as li:
        print(li)

    print(l1.remover(13))
    print(l1)

    print(l1.remover(1))
    print(l1)

    print(l1.remover(3))
    print(l1)

    try:
        print(l1.remover(15))
        print(l1)
    except ListaException as li:
        print(li)
