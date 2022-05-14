'''
Classe para instanciação de nós que vão ficar na memória
'''

class Node:
    def __init__(self,data:object):
        self.__data = data
        self.__leftChild = None
        self.__rightChild = None

    @property
    def data(self)->object:
        return self.__data

    @data.setter
    def data(self, newData:object):
        self.__data = newData

    @property
    def leftChild(self)->'Node':
        return self.__leftChild

    @leftChild.setter
    def leftChild(self, newLeftChild:object):
        self.__leftChild = newLeftChild

    @property
    def rightChild(self)->'Node':
        return self.__rightChild

    @rightChild.setter
    def rightChild(self, newRightChild:'Node'):
        self.__rightChild = newRightChild

    def insertLeft(self, data:object):
        if self.__leftChild == None:
            self.__leftChild = Node(data)	

    def insertRight(self,data:object):
        if self.__rightChild == None:
            self.__rightChild = Node(data)

    def __str__(self):
        return str(self.__data)

    def hasLeftChild(self)->bool:
        return self.__leftChild != None

    def hasRightChild(self)->bool:
        return self.__rightChild != None
        
	    
'''
Classe para a instanciação de Árvores Binárias
Autor: Alex Sandro
Data da última modificação: 11/05/2022
'''
class BinaryTree:
    # constructor that initializes an empty Tree 
    def __init__(self, data_root:object):
        self.__root = Node(data_root)
        self.string = ""

    def getRoot(self)->'Node':
        '''Obtem a referência para o nó "root"'''
        return self.__root

    def addLeft(self, target_key, data )->bool:
        target = self.getNode(target_key)
       
        if target.leftChild is None:
            target.leftChild = Node(data)

    def addRight(self, target_key, data )->bool:
        target = self.getNode(target_key)

        if target.rightChild is None:
            target.rightChild = Node(data)
        
    def getNode(self, key ):
        #NO = NONE QUANDO O NO É IGUAL A RAIZ
        return self.__getNode(key, self.getRoot())

    def __getNode(self, key, node:Node)->Node:
        if (node == None):
            return None # Nao encontrou a chave

        if ( key == node.data):
            return node

        returnedNode = self.__getNode( key, node.leftChild)

        if ( returnedNode):
            return returnedNode
        else:
            return self.__getNode( key, node.rightChild)

    def search(self, chave:object )->bool:
        '''Realiza uma busca na árvore pelo nó cuja carga é igual à chave
           passada como argumento.
           Returns
           ---------
           True: caso a chave seja encontrada na árvore
           False: caso a chave não esteja na árvore
        '''
        return self.__searchData(chave, self.__root)
    
    def __searchData(self, chave, node):
        if (node == None):
            return False # Nao encontrou a chave
        if ( chave == node.data):
            return True
        elif ( self.__searchData( chave, node.leftChild)):
            return True
        else:
            return self.__searchData( chave, node.rightChild)

    def preorderTraversal(self):
        '''Exibe os nós da árvore com percurso em pré-ordem'''
        self.__preorder(self.__root)

    def inorderTraversal(self):
        '''Exibe os nós da árvore com percurso em in-ordem'''
        self.__inorder(self.__root)

    def postorderTraversal(self):
        '''Exibe os nós da árvore com percurso em pós-ordem'''
        self.__postorder(self.__root)
        
    def __preorder(self, node):
        if( node == None):
            return

        print(f'{node.data}')

        self.__preorder(node.leftChild)
        self.__preorder(node.rightChild)

    def __inorder(self, node):
        if( node == None):
            return
        self.__inorder(node.leftChild)
        print(f'{node.data} ',end='')
        self.__inorder(node.rightChild)

    def __postorder(self, node):
        if( node == None):
            return
        self.__postorder(node.leftChild)
        self.__postorder(node.rightChild)
        print(f'{node.data} ',end='')

    def deleteTree(self):
        '''Elimina todos os nós da árvore'''
        # garbage collector fará o trabalho de eliminação dos nós
        # abandonados 
        self.__root = None

    def __deleteNode(self,root, key):

        if root is None: 
            return
        elif root.leftChild == None and root.rightChild == None:
            return
        
        if root.leftChild == None:
            if root.rightChild.data == key:
                root.rightChild = None
        elif root.rightChild == None:
            if root.leftChild.data == key:
                root.leftChild = None
