import socket

HOST = '127.0.0.1'
PORT = 6000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor = (HOST, PORT)

while True:
    msg = input('Digite algo:')
    udp.sendto(msg.encode(), servidor)
    msg_servidor, servidor = udp.recvfrom(1024)
    print(msg_servidor.decode())