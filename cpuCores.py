import cpuinfo
import psutil


def getCpu():
    cpuInfo = cpuinfo.get_cpu_info()
    cpuPercent = psutil.cpu_percent(interval=0, percpu=True)

    cpu = {
        'cpu_info': cpuInfo,
        'cpu_percent': cpuPercent
    }

    return cpu
