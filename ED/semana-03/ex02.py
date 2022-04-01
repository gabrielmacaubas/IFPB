class Aluno:
    def __init__(self, m: int, nom: str):
        self.matricula = m
        self.nome = nom
        self.notas = list()

    def get_nome(self):
        return self.nome

    def get_matricula(self):
        return f'Matrícula: {self.matricula}'

    def media(self):
        return sum(self.notas) / len(self.notas)

    def set_nome(self, n: str):
        self.nome = n

    def adiciona_nota(self, nota: str):
        self.notas.append(nota)


aluno = Aluno(202112123, "macaubas")
print(aluno.nome)
aluno.set_nome("gabriel")
print(aluno.nome)
aluno.adiciona_nota(10)
aluno.adiciona_nota(9)
aluno.adiciona_nota(8)
aluno.adiciona_nota(7)
print(aluno.notas)
print(aluno.media())
print(aluno.matricula)
