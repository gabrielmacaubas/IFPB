from node import Node
from binary_tree import BinaryTree

if __name__ == "__main__":
    raiz = Node('A')
    raiz.esq = Node('B')
    raiz.dir = Node('C')

    p = raiz.esq
    q = raiz.dir

    p.esq = Node('D')
    p = p.esq

    p.dir = Node('G')

    q.esq = Node('E')
    q.dir = Node('F')

    q = q.esq

    q.esq = Node('H')
    q.dir = Node('I')

    arvore = BinaryTree()
    arvore.em_ordem(raiz)