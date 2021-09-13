import socket
import os
import sys
import pickle
import properties as CONSTANTS
import pid as pidInfo
import disk as diskInfo
import cpuCores as CpuCoresInfo
import memory as MemoryInfo
import network as NetworkInfo
import resume as ResumeInfo
import file as FileInfo
import host as HostInfo


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.bind((CONSTANTS.HOST, CONSTANTS.PORT))
    sock.listen()

    print(
        f'Servidor iniciado em {CONSTANTS.HOST} ({CONSTANTS.HOST_NAME}) na porta {CONSTANTS.PORT}')

    (clientSock, clientAddr) = sock.accept()
    print(f'Conectado estabelecida - {str(clientAddr)}')

    while True:
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
            memory = MemoryInfo.getMemoryInfo()
            memory = pickle.dumps(memory)

            clientSock.send(memory)

        if message == 'network':
            network = NetworkInfo.getNetwork()
            network = pickle.dumps(network)

            clientSock.send(network)

        if message == 'resume':
            resume = ResumeInfo.getResume()
            resume = pickle.dumps(resume)

            clientSock.send(resume)

        if message == 'simple-files':
            simpleFiles = FileInfo.getSimpleFiles()
            simpleFiles = pickle.dumps(simpleFiles)

            clientSock.send(simpleFiles)

        if message == 'detailed-files':
            detailedFiles = FileInfo.getDetailedFiles()
            detailedFiles = pickle.dumps(detailedFiles)

            clientSock.send(detailedFiles)

        if message == 'pid':
            pid = pidInfo.getPid()
            pid = pickle.dumps(pid)

            clientSock.send(pid)
            
        if message == 'host':
            host = HostInfo.getHosts()
            host = pickle.dumps(host)

            clientSock.send(host)

        if message == 'close-application':
            clientSock.close()
            print(f'Conexão encerrada - {str(clientAddr)}')
            break

    sock.close()
except Exception as error:
    print(str(error))
    pass
