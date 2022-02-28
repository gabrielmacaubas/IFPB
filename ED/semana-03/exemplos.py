class Pessoa:
    
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
    
    def get_idade(self):
        return self._idade
    
    def set_idade(self, nova_idade):
        self._idade = nova_idade
    
aluno = Pessoa('Carlos', 19)
print('Nome do aluno:', aluno._nome)
aluno.set_idade(-3)
print('Idade do aluno:', aluno.get_idade())
