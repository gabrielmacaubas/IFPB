from pilha_sequencial import Pilha

p = Pilha(tamanho=10)
#assert p.obter_quantidade() == 0
p.empilha(3)
#assert p.desempilha() == 3
p.empilha(4)
p.empilha(5)
p.empilha(6)
print(p.desempilha())
print(p.desempilha())
print(p.desempilha())
print(p.desempilha())
print(p.desempilha())

#assert p.desempilha() == 6
#assert p.desempilha() == 5
#assert p.desempilha() == 4
#assert p.obter_quantidade() == 0
# print(p.desempilha())
# assert p.obter_quantidade() == 0
#p.desempilha()
