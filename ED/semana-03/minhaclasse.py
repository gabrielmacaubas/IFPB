class Curso:
    numVagas = 40
    def __init__(self, nome='', periodo = '2020.2'):
        self.nome = nome
        self.periodo = periodo
        self.vagas = Curso.numVagas
        Curso.numVagas += 5
    
    def show(self):
        print(self.nome,',', self.periodo)

#main
curso1 = Curso('Computação','2020.2')
curso1.show()
print(curso1.vagas)
print(Curso.numVagas)
curso2 = Curso('Administração','2020.2')
curso2.show()
print(curso2.vagas)
print(Curso.numVagas)
curso3 = Curso('Biologia','2020.2')
print(curso3.vagas)
print(Curso.numVagas)