class Node:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None

class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0
    
    def empilhar(self, valor):
        if self.topo is None:
            self.topo = Node(valor)
            self.tamanho += 1

        else:         
            novo_topo = Node(valor)
            novo_topo.prox = self.topo
            self.topo = novo_topo
            self.tamanho += 1

            """
            topo 2
            topo 1
            topo 0            
                    topo -1

            topo -1
            topo -2
            """
    
    #def desempilhar(self):
    
    def exibir_pilha(self):
        print(self.__str__())
    
    def __str__(self):
        string = ""
        topo_atual = self.topo
        for i in range(self.tamanho):
            string += str(topo_atual.valor)
            topo_atual = topo_atual.prox

            
        return string


if __name__ == "__main__":
    p = Pilha()
    p.empilhar(1)
    p.empilhar(2)
    p.empilhar(3)
    p.exibir_pilha()