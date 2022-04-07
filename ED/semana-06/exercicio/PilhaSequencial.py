class PilhaException(Exception):

    def __init__(self, msg):
        super().__init__(msg)


class Pilha:

    def __init__(self):
        self.__pilhas = [
            [],
        ]
        self.pilha_atual = 0
        self.interface = ''
        self.opcao = str()

    def mudarOpcao(self):
        self.opcao = str(input("Digite sua opção: "))
        if self.opcao.lower() == "e":
            self.empilha(input("Insira um dado: "))

        elif self.opcao.lower() == "d":
            print(f"O elemento: {self.desempilha()} foi desempilhado")

        elif self.opcao.lower() == "t":
            ...
        elif self.opcao.lower() == "o":
            ...
        elif self.opcao.lower() == "v":
            ...
        elif self.opcao.lower() == "r":
            ...
        elif self.opcao.lower() == "n":
            ...
        elif self.opcao.lower() == "z":
            ...
        elif self.opcao.lower() == "c":
            ...
        elif self.opcao.lower() == "m":
            ...
        elif self.opcao.lower() == "n":
            ...

        else: # sair
            ...

    def estaVazia(self):
        return len(self.getPilhas()[self.pilha_atual]) == 0

    def tamanho(self):
        return len(self.getPilhas()[self.pilha_atual])

    def quantidadePilhas(self):
        return len(self.getPilhas())

    def elemento(self, posicao):
        try:
            assert posicao > 0
            return self.getPilha()[posicao - 1]
        except IndexError:
            raise PilhaException(f'Posicao {posicao} invalida para a Pilha')
        except TypeError:
            raise PilhaException(f'O tipo de dado para posicao não é um número inteiro')
        except AssertionError:
            raise PilhaException(f'A posicao deve ser um número maior que zero')
        except:
            raise

    def busca(self, valor):
        try:
            return self.getPilha().index(valor) + 1
        except ValueError:
            raise PilhaException(f'O valor {valor} não está armazenado na pilha')
        except:
            raise

    def topo(self):
        if self.tamanho() == 0:
            return '_'

        return self.getPilha()[-1]

    def empilha(self, valor):
        self.getPilha().append(valor)

    def desempilha(self):
        try:
            return self.getPilha().pop()
        except IndexError:
            raise PilhaException(f'Pilha Vazia. Não é possível efetuar a remoção')
        except:
            raise

    def imprimir(self):
        print(self.__str__())

    def getPilhas(self):
        return self.__pilhas

    def getPilha(self):
        return self.__pilhas[self.pilha_atual]

    def __str__(self):
        blue = '\033[34m'
        red = '\033[31m'
        bold = '\033[1m'
        stop = '\033[m'
        lines = '=' * 37

        self.interface = f'''
{bold}Editor de Pilha v1.2{stop}
{lines}
{bold}Pilha Selecionada: {blue}{self.pilha_atual + 1}{stop} de {self.quantidadePilhas()}
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

        return self.interface


if __name__ == '__main__':
    p = Pilha()
    p.imprimir()
    while True:
        try:

            p.mudarOpcao()
            print()
        except PilhaException as pe:
            print(pe)
        except Exception as e:
            print('Nossos engenheiros vao analisar esse problema')
        except:
            print('FIM')
