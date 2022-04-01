class Relogio:

    def __init__(self, seg):
        self.seg = seg

    @property
    def minutos(self):
        print('obtendo valor')
        return self.seg // 60

    @minutos.setter
    def minutos(self, valor):
        print('setando valor')
        self.seg = valor * 60

    @property
    def horas(self):
        return self.minutos // 60

    @horas.setter
    def horas(self, valor):
        print('cascata')
        self.minutos = valor * 60
