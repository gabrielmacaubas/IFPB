class Data:
    def __init__(self):
        self.__dia = int()
        self.__mes = int()
        self.__ano = int()

    def __str__(self):
        return f'{self.__dia}/{self.__mes}/{self.__ano}'

    @property
    def dia(self):
        return self.__dia

    @property
    def mes(self):
        return self.__mes

    @property
    def ano(self):
        return self.__ano

    @dia.setter
    def dia(self, d):
        self.__dia = d

    @mes.setter
    def mes(self, m):
        self.__mes = m

    @ano.setter
    def ano(self, a):
        self.__ano = a

# Programa Principal
data = Data()
data.dia = 8
data.mes = 3
data.ano = 2022

print(data)
