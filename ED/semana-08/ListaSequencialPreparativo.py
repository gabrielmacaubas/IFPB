class ListaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)




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
        '''
        for i in range(self.__dados):
            if self.__dados[i] == dado:
                return i+1
        return None
        '''
        try:
            return self.__dados.index(dado) + 1
        except ValueError:
            raise ListaException(f'O valor {dado} não se encontra na lista')
        except:
            raise





    # operacao que recebe a posicao de um elemento da lista e retorna
    # o conteúdo (dado) que está armazenado
    def elemento(self, posicao):
        # valor negativo?
        # posicao invalida IndexError
        # posicao com o tipo de dado diferente de int TypeError
        try:
            assert posicao > 0
            return self.__dados[posicao-1]
        except TypeError:
            raise ListaException('O argumento posicao deve ser um valor do tipo inteiro')
        except IndexError:
            raise ListaException('A posicao informada para consulta é inválida')
        except AssertionError:
            raise ListaException('Posicao negativa não é válida para a lista')
        except:
            raise

    # função que insere um dado na lista na posicao indicada (posição válida)
    def inserir(self, posicao, dado):
        try:
            assert posicao > 0
            self.__dados.insert(posicao-1, dado)
        except TypeError:
            raise ListaException('O argumento posicao deve ser um valor do tipo inteiro')
        except IndexError:
            raise ListaException('A posicao informada para consulta é inválida')
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
            valor = self.__dados[posicao-1]
            del self.__dados[posicao-1]
            return valor
        except TypeError:
            raise ListaException('O argumento posicao deve ser um valor do tipo inteiro')
        except IndexError:
            raise ListaException('A posicao informada para consulta é inválida')
        except AssertionError:
            raise ListaException('Posicao negativa não é válida para a lista')
        except:
            raise

    # método especial que retorna a descrição interna do objeto
    def __str__(self):
        return self.__dados.__str__()
    
    # método que imprime o conteúdo da Lista Sequencial
    def imprimir(self):
        print(self.__str__())

    # método que altera o conteúdo armazenado em uma determinada posição da lista
    def modificar(self, posicao, novoValor):
        try:
            assert posicao > 0
            if( self.vazia()):
                raise ListaException('Lista Vazia. Não é possível remover elementos')
            self.__dados[posicao-1] = novoValor
            return True
        except TypeError:
            raise ListaException('O argumento posicao deve ser um valor do tipo inteiro')
        except IndexError:
            raise ListaException('A posicao informada para consulta é inválida')
        except AssertionError:
            raise ListaException('Posicao negativa não é válida para a lista')
        except:
            raise

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

    #l1.inserir(-10,99)
    print(l1)

    try:
        #print(l1.busca(55))
        #print(l1.elemento(5))
        #l1.inserir(5,111)
        #l1.remover(1)
        l1.modificar(100, 999)
        print(l1)
    except ListaException as li:
        print(li)
        

