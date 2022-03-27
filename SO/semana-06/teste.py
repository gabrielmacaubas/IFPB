import threading
from threading import Thread

class Numero:

    def __init__(self, valor=0):
        self.valor = valor


def contador(n):
    n.valor += 1
    print(threading.current_thread().getName(), n.valor)


numero = Numero()

t1 = threading.Thread(target=contador, args=(numero,))
t2 = threading.Thread(target=contador, args=(numero,))

print('num final', numero.valor)
t1.start()
t2.start()


class Contador(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        print('thread criada via classe')



t3 = Contador()
t3.start()