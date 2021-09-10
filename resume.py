import cpuinfo
import psutil


def getResume():
    memoryInfo = psutil.virtual_memory()
    cpuInfo = cpuinfo.get_cpu_info()
    ip = psutil.net_if_addrs()
    disk = psutil.disk_usage('/')

    resume = {
        'cpu_name': cpuInfo['brand_raw'],
        'ip': ip['Ethernet'][1][1],
        'disk_total': disk[0],
        'disk_percent': disk[3],
        'memory_total': memoryInfo[0],
        'memory_use': memoryInfo[3],
        'memory_percent': memoryInfo.percent
    }

    return resume
