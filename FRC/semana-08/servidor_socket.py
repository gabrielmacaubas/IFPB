import socket

HOST = "127.0.0.1"
PORT = 65000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
conexao, endereco = s.accept()
with conexao:
        print(f'Recebi conexão de {endereco}')
        while True:
            data = conexao.recv(1024)
            
            if not data:
                break

            print(f'dado recebido: {data}')
            conexao.sendall(f"Tamanho da mensagem: {len(data)}".encode())
