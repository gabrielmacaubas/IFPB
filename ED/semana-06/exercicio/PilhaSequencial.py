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
            return f"O dado {self.topo()} foi empilhado!"

        elif self.opcao.lower() == "d":
            return f"O elemento: {self.desempilha()} foi desempilhado!"

        elif self.opcao.lower() == "t":
            return f"A pilha {self.pilha_atual + 1} -> {self.getPilha()} tem tamanho {self.tamanho()}!"
            
        elif self.opcao.lower() == "o":
            return f"\033[1m[ {self.topo()} ] <- topo\033[m"
             
        elif self.opcao.lower() == "v":
            if self.estaVazia():
                return "A pilha está vazia!"

            return f"A pilha não está vazia. Tem o tamanho {self.tamanho()}!"

        elif self.opcao.lower() == "r":
            self.getPilhas().append([])


            return "Pilha criada com sucesso!"

        elif self.opcao.lower() == "n":
            ...
        elif self.opcao.lower() == "z":
            ...
        elif self.opcao.lower() == "c":
            ...
        elif self.opcao.lower() == "m":
            pilha_escolhida = int(input("Pilha escolhida: "))
            self.pilha_atual = pilha_escolhida - 1

            return f"\033[1mPilha Selecionada: \033[34m{self.pilha_atual + 1}\033[m de {self.quantidadePilhas()}"

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
            raise PilhaException(f'Pilha Vazia. Não é possível efetuar a remoção\n')
        except:
            raise

    def getPilhas(self):
        return self.__pilhas

    def getPilha(self):
        return self.__pilhas[self.pilha_atual]

    def imprimir(self):
        print(self.__str__())

    def __str__(self):
        self.interface = f'''
\033[1mEditor de Pilha v1.2\033[m
{'=' * 37}
\033[1mPilha Selecionada: \033[34m{self.pilha_atual + 1}\033[m de {self.quantidadePilhas()}
\033[1m[ {self.topo()} ] <- topo\033[m
{'=' * 37}
(e) Empilhar
(d) Desempilhar
(t) Tamanho
(o) Obter elemento do topo
(v) Teste de pilha vazia
\033[31m(r) Criar nova pilha
(n) Inverter os elementos da pilha
(z) Esvaziar a pilha
(c) Concatenar duas pilhas\033[m
(m) Escolher outra pilha
\033[31m(n) Conversão dec/bin
\033[mE(a) Atualizar interface
(s) Sair
{'=' * 37}'''

        return self.interface


if __name__ == '__main__':
    p = Pilha()
    p.imprimir()

    while True:

        try:
            print(p.mudarOpcao())
            print()
        except PilhaException as pe:
            print(pe)
        except Exception as e:
            print('Nossos engenheiros vao analisar esse problema')
        except:
            print('FIM')
