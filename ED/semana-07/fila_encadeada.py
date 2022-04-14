class FilaException(Exception):
    pass


class No:

    def __init__(self, valor: int):
        self.valor: int = valor
        self.proximo = None


class Fila:

    def __init__(self):
        self.inicio: No = None
        self.fim: No = None
        self.tamanho: int = 0
    
    def esta_vazia(self):
        return self.inicio is None
    
    def obter_tamanho(self):
        return self.tamanho

    def enfileirar(self, valor: int):
        no = No(valor)

        if self.esta_vazia():
            self.inicio = no
        else:
            self.fim.proximo = no
        
        self.fim = no
        self.tamanho += 1

    def desenfileirar(self) -> int:
        if self.esta_vazia():
            raise FilaException('fila vazia')

        primeiro = self.inicio

        self.inicio = self.inicio.proximo
        self.tamanho -= 1

        return primeiro.valor

    @classmethod
    def combina(cls, fres, f1, f2):
        for i in range(f1.obter_tamanho() + f2.obter_tamanho()):
            if i % 2 == 0:
                fres.enfileirar(f1.desenfileirar())

            else:
                fres.enfileirar(f2.desenfileirar())

    def imprimir(self):
        no = self.inicio

        while no:
            print(f'{no.valor}, ', end='')
            no = no.proximo
            
        print()


if __name__ == "__main__":
    f1 = Fila()
    f2 = Fila()
    fres = Fila()

    f1.enfileirar(2.1)
    f1.enfileirar(4.5)
    f1.enfileirar(1.0)
    f2.enfileirar(7.2)
    f2.enfileirar(3.1)
    f2.enfileirar(9.8)
    f1.imprimir()
    f2.imprimir()

    Fila.combina(fres, f1, f2)
    fres.imprimir()