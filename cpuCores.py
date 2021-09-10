from os import cpu_count
import cpuinfo
import psutil


def getCpu():
    cpuInfo = cpuinfo.get_cpu_info()
    cpuBrand = cpuInfo['brand_raw']
    cpuArchitecture = cpuInfo['arch']
    cpuBits = cpuInfo['bits']
    cpuPercent = psutil.cpu_percent(interval=0, percpu=True)
    cpuFrequency = psutil.cpu_freq().current
    cpuCountAllCores = psutil.cpu_count()
    cpuCountPhysicalCores = psutil.cpu_count(logical=False)

    cpu = {
        'cpu_brand': cpuBrand,
        'cpu_architecture': cpuArchitecture,
        'cpu_bits': cpuBits,
        'cpu_percent': cpuPercent,
        'cpu_frequency': cpuFrequency,
        'cpu_count_all_cores': cpuCountAllCores,
        'cpu_count_physical_cores': cpuCountPhysicalCores
    }

    return cpu
