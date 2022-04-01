from threading import Thread
import time

global texto
texto = ''

global nova_parte
nova_parte = ''

global tamanho_anterior
tamanho_anterior = 0


def pega_dados():
    global texto
    global nova_parte
    while True:
        nova_parte = input()
        texto += nova_parte.replace('\n', '')


def calcula_letras():
    global texto
    global tamanho_anterior
    while True:
        if len(texto) > tamanho_anterior:
            print('Texto: [', texto, ']')
            print('#caracteres:', len(texto), '\n')
            tamanho_anterior = len(texto)
            tamanho_anterior = len(texto)
        time.sleep(0)


def salda_dados():
    global texto
    global nova_parte
    global tamanho_anterior
    while True:
        if len(texto) > tamanho_anterior:
            with open('arq_temp.txt', 'a') as f:
                f.write(f'\n{nova_parte}')
                tamanho_anterior = len(texto)
        time.sleep(0)


# sem threads
# pega_dados()
# calcula_letras()


t_escrita = Thread(target=pega_dados)
t_estatica = Thread(target=calcula_letras)
t_salvamento = Thread(target=salda_dados)

t_escrita.start()
t_estatica.start()
t_salvamento.start()

t_escrita.join()
t_estatica.join()
t_salvamento.join()