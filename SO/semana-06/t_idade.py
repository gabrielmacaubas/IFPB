from threading import Thread
from time import sleep

class Usuario:
    def __init__(self, idade):
        self.idade = idade


u = Usuario(30)


def incrementa_idade(num_thread, usuario):
    while True:
        usuario.idade += 1
        print('thread', num_thread, 'idade:', usuario.idade)
        print('\n')
        # sleep(0.5)


t1 = Thread(target=incrementa_idade, args=(1, u,))
t2 = Thread(target=incrementa_idade, args=(2, u,))

t2.start()
t1.start()
