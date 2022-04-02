class PilhaException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class PilhaSequencial:
    def __init__(self):
        self.__pilhas = [
            [1],
        ]
        self.__pilha_atual = int()
        self.__interface = ''
        self.__opcao = str()

    def mudar_opcao(self):
        self.__opcao = input("Digite sua opção: ")
        if self.__opcao.lower() == "e":
            ...
        if self.__opcao.lower() == "d":
            ...
        if self.__opcao.lower() == "t":
            ...
        if self.__opcao.lower() == "o":
            ...
        if self.__opcao.lower() == "v":
            ...
        if self.__opcao.lower() == "r":
            ...
        if self.__opcao.lower() == "n":
            ...
        if self.__opcao.lower() == "z":
            ...
        if self.__opcao.lower() == "c":
            ...
        if self.__opcao.lower() == "m":
            ...
        if self.__opcao.lower() == "n":
            ...
        if self.__opcao.lower() == "s":
            ...



    def vazia(self):
        return len(self.__pilhas[self.__pilha_atual]) == 0

    def tamanho_pilha(self):
        return len(self.__pilhas[self.__pilha_atual])

    def quantidade_pilhas(self):
        return len(self.__pilhas)

    def topo(self):

        return self.__pilhas[0][0]


    def inserir(self, dado):
        self.__pilhas[0].insert(0, dado)

    def remover(self):
        return self.__pilhas.pop(0)

    def __str__(self):
        blue = '\033[34m'
        red = '\033[31m'
        bold = '\033[1m'
        stop = '\033[m'
        lines = '=' * 37


        self.__interface = f'''{bold}Editor de Pilha v1.2{stop}
{lines}
{bold}Pilha Selecionada: {blue}{self.__pilha_atual}{stop} de {self.quantidade_pilhas()}
{bold}[ {self.topo()} ] <- topo{stop}
{lines}
(e) Empilhar
(d) Desempilhar
(t) Tamanho
(o) Obter elemento do topo
(v) Teste de pilha vazia
{red}(r) Criar nova pilha
(n) Inverter os elementos da pilha
(z) Esvaziar a pilha
(c) Concatenar duas pilhas{stop}
(m) Escolher outra pilha
{red}(n) Conversão dec/bin
{stop}(s) Sair
{lines}'''

        return self.__interface

    def imprimir(self):
        print(self.__str__())


if __name__ == '__main__':
    p = PilhaSequencial()

    print(p)

    p.mudar_opcao()