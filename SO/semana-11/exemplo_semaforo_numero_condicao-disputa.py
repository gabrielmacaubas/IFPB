from threading import Semaphore, Thread
import time

# Prof. Gustavo Wagner, gugawag@gmail.com
# IFPB - Sistemas Operacionais
# Explicacao: programa desenvolvido para demonstrar condicao de disputa. Metodos p1 e p2, indefinidamente, incrementam
#             a variavel global 'numero'. Como nao hah exclusao mutua, pode haver condicao de corrida.

print("Gabriel Macaúbas Melo")

numero = 0
mutex = Semaphore(1)

# Codigo estah pulando numeros, e repetindo numeros entre threads

def p1():
    global numero
    
    while True:
        mutex.acquire()

        numero += 1
        print('P1:', numero)

        mutex.release()

        time.sleep(1) # usado apenas para forcar trocar contexto entre threads e visualizar condicao de disputa

def p2():
    global numero
    
    while True:
        mutex.acquire()

        numero += 1 
        print('P2:', numero)

        mutex.release()

        time.sleep(1)  # usado apenas para forcar trocar contexto entre threads e visualizar condicao de disputa

t_p1 = Thread(target=p1)
t_p2 = Thread(target=p2)

t_p1.start()
t_p2.start()
