class Aluno:
    def __init__(self, n, i, m):
        self.nome = n
        self.idade = i
        self.matricula = m

a = Aluno('Thiago',41,'20202370001')

print('Nome do aluno:',a.nome)
print('Idade do aluno:',a.idade)
print('Matricula do aluno:',a.matricula)