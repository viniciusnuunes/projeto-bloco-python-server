import os
import subprocess
import platform
import psutil
import nmap
import threading


def getHosts():
    hostNamesDict = dict()
    hostPortDict = dict()
    protocolDict = dict()
    portList = []

    def updateHostInfo(host):
        print('Iniciado Host: ' + host)
        try:
            nm.scan(host)

            hostName = nm[host].hostname()

            if hostName:
                hostNamesDict[host] = hostName
            else:
                hostNamesDict[host] = 'Não obtido'

            hostPortDict[host] = host
            protocols = nm[host].all_protocols()

            for protocol in protocols:
                protocolDict[protocol] = protocol

                ports = nm[host][protocol].keys()

                for port in ports:
                    state = nm[host][protocol][port]['state']

                    portList.append({
                        'port': port, 'state': state
                    })

                protocolDict[protocol] = portList

            hostPortDict[host] = protocolDict

            print('Finalizado Host: ' + host)
        except Exception as error:
            print(str(error))
            pass

    ipInfo = psutil.net_if_addrs()['Ethernet'][1][1]

    splitIP = ipInfo.split('.')
    baseIP = ".".join(splitIP[0:3]) + '.'

    validHosts = __getValidHosts(baseIP)

    nm = nmap.PortScanner()

    threadList = []

    print('Iniciando extração de dados por Host')
    for host in validHosts:
        t = threading.Thread(target=updateHostInfo, args=(host,))
        t.start()
        threadList.append(t)

    for t in threadList:
        t.join()

    hostsInfos = {
        'hostsNames': hostNamesDict,
        'hostsPorts': hostPortDict
    }

    print('Extração finalizada')

    return hostsInfos


def __getValidHosts(baseIP):
    print("O teste será feito na sub rede com base de IP: ", baseIP)
    print("Mapeando...\r")

    validHosts = []
    returnedCodes = dict()

    for i in range(1, 255):
        i_str = str(i)
        returnedCodes[baseIP + i_str] = __pingCode(baseIP + i_str)

        if returnedCodes[baseIP + i_str] == 0:
            validHosts.append(baseIP + i_str)

    print("Mapeamento pronto")
    print("Os host válidos são: ", validHosts)

    return validHosts


def __pingCode(hostname):
    """Usa o utilitario ping do sistema operacional para encontrar o host. ('-c 5') indica,
    em sistemas linux, que deve mandar 5 pacotes. ('-W 3') indica, em sistemas linux,
    que deve esperar 3 milisegundos por uma resposta. Esta funcao retorna o codigo de resposta do ping """

    platformName = platform.system()
    args = []

    if platformName == "Windows":
        args = ["ping", "-n", "1", "-l", "1", "-w", "100", hostname]

    else:
        args = ['ping', '-c', '1', '-W', '1', hostname]

    code = subprocess.call(args,
                           stdout=open(os.devnull, 'w'),
                           stderr=open(os.devnull, 'w'))
    return code
