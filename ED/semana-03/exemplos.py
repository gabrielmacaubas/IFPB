class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, nova_idade):
        if nova_idade >= 0:
            self._idade = nova_idade
    
aluno = Pessoa('Carlos', 19)
print('Nome do aluno:', aluno._nome)
aluno.idade = (-3)
print('Idade do aluno:', aluno.idade)
