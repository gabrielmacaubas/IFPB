import meu_so

class Lista:
    
    def __init__(self):
        self.__tamanho = 0
        self.__dados = meu_so.alocar(tamanho)
  
    def atribuir_elemento(self, posicao, valor):
        self.__dados[posicao] = valor

    def obter_elemento(self, posicao):
        return self.__dados[posicao]

    def imprimir(self):
        print(self.__dados)
    
    def obter_tamanho(self):
        return self.__tamanho

    def redimensiona(self, quantidade):
        if quantidade > self.__tamanho:
            self.__dados = meu_so.realocar(
                self.__dados,
                quantidade
            )
        elif quantidade < self.__tamanho:
            indice = 0
            dados = meu_so.alocar(quantidade)
            for elemento in self.__dados[:quantidade]:
                dados[indice] = elemento
                indice += 1
            self.dados = dados
        self.__tamanho = quantidade

    def deslocar_a_direita(self, posicao):
        indice = posicao
        for elemento in self.__dados[posicao:-1]:
            self.__dados[indice+1] = elemento
            indice += 1
    
    def deslocar_a_esquerda(self, posicao):
        indice = posicao
        for elemento in self.__dados[posicao+1:]:
            self.__dados[indice] = elemento
            indice += 1

    def insereNoFim(self, valor):
        # .append
        self.redimensiona(self.obter_tamanho() + 1)
        self.__dados[self.obter_tamanho() - 1] = valor

    def insereNoComeco(self, valor):
        self.insereNaPosicao(0, valor)

    def insereNaPosicao(self, posicao, valor):
        self.redimensiona(self.obter_tamanho + 1)  
        self.deslocar_a_direita(posicao)
        self.__dados[posicao] = valor

    def removerDoFim(self):
        self.redimensiona(self.obter_tamanho() - 1)
    
    def removerDoInicio(self):
        self.deslocar_a_esquerda(0)
        self.redimensiona(self.obter_tamanho() - 1)

    def removerDaPosicao(self, posicao):
        self.deslocar_a_esquerda(posicao)
        self.redimensiona(self.obter_tamanho() - 1)