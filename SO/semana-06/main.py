from threading import Thread
from time import sleep

n = 10


def f1(nome_thread):
    global n
    sleep(0.1)
    n += 1
    print(nome_thread, n)


def f2(nome_thread):
    global n
    n += 1
    print(nome_thread, n)


t1 = Thread(target=f1, args=(1,))
t1.start()
t2 = Thread(target=f2, args=(2,))
t2.start()

print('Thread main')
