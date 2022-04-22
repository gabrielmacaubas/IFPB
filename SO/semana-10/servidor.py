import socket
from pathlib import Path

HOST = '127.0.0.1'
PORT = 6000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)

udp.bind(orig)

print('Servidor no ar...')

while True:
    msg, cliente = udp.recvfrom(1024)
    print('Recebi do cliente', cliente, msg.decode())
    # LERDIR /tmp/tu/eu/
    # CRIADIR /tmp/eu
    resposta = ''
    comando_quebrado = msg.decode().split()
    if comando_quebrado[0] == 'LERDIR':
        caminho = comando_quebrado[1]
        p = Path(caminho)
        for arq in p.iterdir():
            resposta += str(arq) + '\n'
    else:
        print('Ainda não conheço esse comando!')
    udp.sendto(resposta.encode(), cliente)

udp.close()