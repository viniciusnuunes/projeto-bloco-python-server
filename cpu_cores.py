import cpuinfo
import psutil


def getCpu():
    cpu_info = cpuinfo.get_cpu_info()
    cpu_percent = psutil.cpu_percent(interval=0, percpu=True)

    cpu = {
        'cpu_info': cpu_info,
        'cpu_percent': cpu_percent
    }

    return cpu
