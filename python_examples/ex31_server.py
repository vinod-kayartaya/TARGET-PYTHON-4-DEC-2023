from socket import socket, AF_INET, SOCK_STREAM
import time
from threading import Thread


def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    addr = ('192.168.1.23', 1234)
    server_socket.bind(addr)
    server_socket.listen(5)
    print(f'server application started at address {addr}')
    while True:
        print('waiting for a client to connect...')
        client_socket, client_addr = server_socket.accept()
        Thread(target=handle_client, args=(client_socket, client_addr)).start()


def handle_client(client_socket, client_addr):
    print(f'got connection from a client at address {client_addr}')
    username = client_socket.recv(1024).decode('ascii')
    msg = f'Hello {username}. Welcome to networking in Python'
    client_socket.send(msg.encode('ascii'))
    time.sleep(20)
    client_socket.close()


if __name__ == '__main__':
    main()
