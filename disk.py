import psutil


def getDiskUsageInfo():
    disk = psutil.disk_usage('/')

    return disk


getDiskUsageInfo()
