class Node:
    def __init__(self,dado):
        self.dado = dado
        self.esq = None
        self.dir = None

    def __str__(self):
        return str(self.dado)


class ArvoreBinaria:        
    def __init__(self, root):
        self.__root = Node(root)
        self.__tamanho = 1
        self.__cursor = self.__root


    def estaVazia(self):
        return self.__root == None
        
    def getRoot(self)->Node:
        return self.__root

    def preordem(self):
        self.__preordem(self.__root)

    def __preordem(self, no):
        if no is not None:
            print(no.dado)
            self.__preordem(no.esq)
            self.__preordem(no.dir)

    def inordem(self):
        self.__inordem(self.__root)

    def __inordem(self, no):
        if no is not None:
            self.__inordem(no.esq)
            print(no.dado)
            self.__inordem(no.dir)

    def posordem(self):
        self.__posordem(self.__root)

    def __posordem(self, no):
        if no is not None:
            self.__posordem(no.esq)
            self.__posordem(no.dir)
            print(no.dado)

    def descerEsquerda(self):
        if self.__cursor.esq is not None:
            self.__cursor = self.__cursor.esq

    def descerDireita(self):
        if self.__cursor.dir is not None:
            self.__cursor = self.__cursor.dir

    def getCursor(self):
        return self.__cursor

    def resetCursor(self):
        self.__cursor = self.__root

    def addNoEsquerda(self, dado)->bool:
        # Condições para inserir um nó a esquerda
        # 1) o .esq tem que ser None
        if self.__cursor.esq == None:
            self.__cursor.esq = Node(dado)
            self.__tamanho += 1
            return True
        else:
            return False

    def addNoDireita(self, dado)->bool:
        # Condições para inserir um nó a esquerda
        # 1) o .esq tem que ser None
        if self.__cursor.dir == None:
            self.__cursor.dir = Node(dado)
            self.__tamanho += 1
            return True
        else:
            return False  

    def __len__(self):
        return self.__tamanho

    def busca(self, chave ):
        return self.__busca(chave, self.__root)
    
    def __busca(self, chave, node):
        if (node == None):
            return False # Nao encontrou a chave
        if ( chave == node.dado):
            return True
        elif ( self.__busca( chave, node.esq)):
            return True
        else:
            return self.__busca( chave, node.dir)

    def getNode(self, chave:int ):
        return self.__getNode(chave, self.__root)
    
    def __getNode(self, chave:int, node:Node)->Node:
        if (node == None):
            return None # Nao encontrou a chave
        if ( chave == node.dado):
            return node
        
        noRetornado = self.__getNode( chave, node.esq)
        if ( noRetornado):
            return noRetornado
        else:
            return self.__getNode( chave, node.dir)


if __name__ == '__main__':
    arv = ArvoreBinaria(2)
    print('Criada a árvore')
    arv.addNoEsquerda(7)
    arv.addNoDireita(5)
    print('Raiz: ', arv.getRoot())
    print('Cursor: ', arv.getCursor())
    print('Tamanho: ', len(arv))
    arv.descerEsquerda()
    arv.addNoEsquerda(9)
    arv.descerEsquerda()
    arv.addNoDireita(3)

    print('Raiz: ', arv.getRoot())
    print('Cursor: ', arv.getCursor())
    print('Tamanho: ', len(arv))

    arv.resetCursor()
    arv.descerDireita()
    arv.addNoEsquerda(10)

    print()
    arv.preordem()

    print('Raiz: ', arv.getRoot())
    print('Cursor: ', arv.getCursor())
    print('Tamanho: ', len(arv))

    print('Busca:', arv.busca(3))
    no = arv.getNode(3)
    print('getNode:', no)
