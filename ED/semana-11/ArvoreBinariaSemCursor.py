class NodeException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

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

    def addNoEsquerda(self, chave_no_alvo:int, dado_a_inserir:int )->bool:
        try:
            alvo = self.getNode(chave_no_alvo)
       
            if alvo.esq is None:
                alvo.esq = Node(dado_a_inserir)
                self.__tamanho += 1
        except AttributeError:
            raise NodeException(f"Erro: O nó {chave_no_alvo} não pertence a árvore.")

    def addNoDireita(self, chave_no_alvo:int, dado_a_inserir:int )->bool:
        try:
            
            alvo = self.getNode(chave_no_alvo)

            if alvo.dir is None:
                alvo.dir = Node(dado_a_inserir)
                self.__tamanho += 1
        
        except AttributeError:
            raise NodeException(f"O nó {chave_no_alvo} não pertence a árvore.")

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
    try:
            
        arv = ArvoreBinaria(2)
        print('Criada a árvore')
        arv.addNoEsquerda(4, 7)


        arv.addNoDireita(2, 5)
        arv.addNoEsquerda(7, 9)
        arv.addNoDireita(7, 3)

        arv.addNoEsquerda(5, 10)

        print()
        arv.preordem()

        print('Raiz: ', arv.getRoot())
        print('Tamanho: ', len(arv))

        print('Busca:', arv.busca(3))
        no = arv.getNode(3)
        print('getNode:', no)
    except NodeException as ne:
        print(ne)
