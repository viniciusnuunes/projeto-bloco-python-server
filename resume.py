import cpuinfo
import psutil


def getResume():
    memory_info = psutil.virtual_memory()
    ip = psutil.net_if_addrs()
    disk = psutil.disk_usage('/')
    cpu_info = cpuinfo.get_cpu_info()

    resume = {
        'cpu_name': cpu_info['brand_raw'],
        'ip': ip['Ethernet'][1][1],
        'disk_total': disk[0],
        'memory_total': memory_info[0],
        'memory_use': memory_info[3],
        'memory_percent': memory_info.percent
    }

    return resume
