import socket
import os
import sys
import pickle
import properties as CONSTANTS
import pid as pidInfo
import disk as diskInfo
import cpu_cores as CpuCoresInfo


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.bind((CONSTANTS.HOST, CONSTANTS.PORT))
    sock.listen()

    print(
        f'Servidor iniciado em {CONSTANTS.HOST} ({CONSTANTS.HOST_NAME}) na porta {CONSTANTS.PORT}')

    while True:
        (sock_client, addr_client) = sock.accept()
        print(f'Conectado estabelecida - {str(addr_client)}')

        data = sock_client.recv(CONSTANTS.BUFFER_SIZE)
        data = data.decode('utf-8')
        
        if data == 'cpu':
            cpu = CpuCoresInfo.getCpu()
            cpu = pickle.dumps(cpu)
            
            sock_client.send(cpu)     

        if data == 'pid':
            pid = pidInfo.getPid()
            pid = pickle.dumps(pid)

            sock_client.send(pid)
            
        if data == 'disk':
            disk = diskInfo.getDiskUsage()
            disk = pickle.dumps(disk)
            
            sock_client.send(disk)

        print(f'Conexão encerrada - {str(addr_client)}')
        sock_client.close()
except Exception as error:
    print(str(error))
    sys.exit(1)
