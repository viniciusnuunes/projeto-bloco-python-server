import psutil


def getNetwork():
    ip = psutil.net_if_addrs()

    network = {
        'ip_pc': ip['Ethernet'][1][1],
        'ip_mask': ip['Ethernet'][1][2],
        'ip_physical_addr': ip['Ethernet'][0][1],
        'ip_ipv6_addr': ip['Ethernet'][2][1]

    }

    return network
