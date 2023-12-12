from socket import socket, AF_INET, SOCK_STREAM


def main():
    client_socket = socket(AF_INET, SOCK_STREAM)
    addr = ('192.168.1.23', 1234)
    client_socket.connect(addr)
    print(f'connected to the server at {addr}')
    username = input('Enter your name: ')
    client_socket.send(username.encode('ascii'))
    resp = client_socket.recv(1024)
    msg = resp.decode('ascii')
    print(f'server message: {msg}')
    print('end of client app')


if __name__ == '__main__':
    main()
