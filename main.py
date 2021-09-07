import socket
import os
import sys
import pickle
import properties as CONSTANTS
import pid as pidInfo
import disk as diskInfo
import cpu_cores as CpuCoresInfo
import network as NetworkInfo
import resume as ResumeInfo


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.bind((CONSTANTS.HOST, CONSTANTS.PORT))
    sock.listen()

    print(
        f'Servidor iniciado em {CONSTANTS.HOST} ({CONSTANTS.HOST_NAME}) na porta {CONSTANTS.PORT}')

    while True:
        (clientSock, clientAddr) = sock.accept()
        print(f'Conectado estabelecida - {str(clientAddr)}')

        message = clientSock.recv(CONSTANTS.BUFFER_SIZE)
        message = message.decode('utf-8')

        if message == 'cpu':
            cpu = CpuCoresInfo.getCpu()
            cpu = pickle.dumps(cpu)

            clientSock.send(cpu)

        if message == 'disk':
            disk = diskInfo.getDiskUsage()
            disk = pickle.dumps(disk)

            clientSock.send(disk)

        if message == 'memory':
            memory = CpuCoresInfo.getCpu()
            memory = pickle.dumps(memory)

            clientSock.send(memory)

        if message == 'network':
            network = CpuCoresInfo.getCpu()
            network = pickle.dumps(network)

            clientSock.send(memory)

        if message == 'resume':
            resume = ResumeInfo.getResume()
            resume = pickle.dumps(resume)

            clientSock.send(resume)

        if message == 'pid':
            pid = pidInfo.getPid()
            pid = pickle.dumps(pid)

            clientSock.send(pid)

        clientSock.close()

        print(f'Conexão encerrada - {str(clientAddr)}')
except Exception as error:
    print(str(error))
    pass
