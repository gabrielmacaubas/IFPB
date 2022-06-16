class MatrizEsparsaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Passageiro:
    def __init__(self, nome:str, rg:str):
        self.__nome = nome
        self.__rg = rg
    
    @property
    def nome(self)->str:
        return self.__nome

    def __str__(self):
        return f'{self.__nome} RG {self.__rg}'


class MatrizEsparsa:
    def __init__(self, id:str, linhas:int, colunas:int):
        '''A numeracao das poltronas é definida da seguinte forma:
                      Poltronas
           Fileira 1: 01 02    03 04
           Fileira 2: 05 06    07 08
           ....
        '''
        self.__id = id
        self.__matriz = [ [ None for y in range( colunas ) ] 
             for x in range( linhas ) ]
        self.__passageiros = int()
    
    def tamanho(self)->int:
        '''Retorna a quantidade de células da matriz'''
        return len(self.__matriz) * len(self.__matriz[0])

    def estaVazia(self)->bool:
        return self.__passageiros == 0

    def estaCheio(self)->bool:
        return self.__passageiros == self.tamanho()

    def procurarAssentoDisponivel(self)->int:
        '''Retorna um assento vazio disponível, se houver.
           Se não houver assento disponível, lançar uma exceção'''
        if self.estaCheio():
            raise MatrizEsparsaException('Não há assento disponível.')
        
        else:
            for l in range(len(self.__matriz)):
                for c in range(len(self.__matriz[0])):
                    return (c * len(self.__matriz) + l) + 1

    def pesquisar(self, numero_poltrona:int)->Passageiro:
        '''Retorna os dados do passageiro alocado em um
           determinado assento'''
        l = (numero_poltrona-1) % len(self.__matriz)
        c = (numero_poltrona-1) // len(self.__matriz)

        return self.__matriz[l][c]

    def pesquisaPassageiro(self, nome:str )->int:
        '''Retorna o número da poltrona em que um determinado
           passageiro está ocupando'''
        pass

    def trocarPoltrona(self, poltrona_atual:int, nova_poltrona:int)->bool:
        pass

    def adicionar(self, passageiro: Passageiro, numero_poltrona:int)->bool:
        '''Retorna True se a inserção foi feita com sucesso, ou 
           False caso contrário'''
        if self.pesquisar(numero_poltrona) is None:
            l = (numero_poltrona-1) % len(self.__matriz)
            c = (numero_poltrona-1) // len(self.__matriz)

            self.__matriz[l][c] = passageiro

    def remover(self, numero_poltrona:int)->Passageiro:
        pass

    def esvaziar(self):
        '''Esvazia a matriz esparsa'''
        pass

    def mostrarAssentos(self):
        '''Mostra o status de ocupacao de todos os assentos'''
        pass

    def __str__(self):
        s = ''
        i = 0
        temp = 1
        for j in range(len(self.__matriz[0])):
            s += f'   {temp:>3}'
            temp += len(self.__matriz)
            
        s += '\n'
        for l in self.__matriz:
            i += 1
            s += f'{i}-'
            for c in l:
                if c is None:
                    s += '[   ] '
                else:
                    s += f'[{c.nome[:3].capitalize()}] '
            s+= '\n'
        temp = len(self.__matriz)

        for j in range(len(self.__matriz[0])):
            s += f'   {temp:>3}'
            temp += len(self.__matriz)

        s += f'\n{self.__id}, {self.tamanho()} assentos.'
        return s


if __name__ == '__main__':
    me = MatrizEsparsa('JPA-CG',4,12)
    print(me)
    me.adicionar(Passageiro("samuel", "123"), 6)
    me.adicionar(Passageiro("madu", "456"), 7)
    me.adicionar(Passageiro("gabriel", "789"), 8)
    print()
    print(me)
