class Data:
    def __init__(self, dia=0, mes=0, ano=0):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia

    #@property
    #def dia(self):
        