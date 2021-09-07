import psutil


def getNetwork():
    ip = psutil.net_if_addrs()

    network = {
        'ip_pc': ip['Ethernet'][1][1],
        'ip_mascara': ip['Ethernet'][1][2],
        'ip_end_fisico': ip['Ethernet'][0][1],
        'ip_end_ipv6': ip['Ethernet'][2][1]

    }

    return network
