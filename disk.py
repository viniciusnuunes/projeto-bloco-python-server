import psutil


def getDiskUsage():
    disk = psutil.disk_usage('/')

    disk = {'disk_total': disk[0],
            'disk_use': disk[1],
            'disk_free': disk[2],
            'disk_percent': disk[3]}

    return disk
