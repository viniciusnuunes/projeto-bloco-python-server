import socket
import os
import sys
import pickle
import properties as CONSTANTS

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.bind((CONSTANTS.HOST, CONSTANTS.PORT))
    sock.listen()

    print(f'Servidor iniciado em {CONSTANTS.HOST} ({CONSTANTS.HOST_NAME}) na porta {CONSTANTS.PORT}')

    while True:
        (sock_client, addr_client) = sock.accept()
        print(f'Conectado a: {str(addr_client)}')

        data = sock_client.recv(CONSTANTS.BUFFER_SIZE)
        data = data.decode('utf-8')

        print(data)

        print(f'Encerrando conexão com: {str(addr_client)}')
        sock_client.close()
except Exception as error:
    print(str(os.error))
    sys.exit(1)
