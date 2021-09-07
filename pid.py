import psutil
import random
import time


def getPid():
    pidList = psutil.pids()
    pidAleatory = random.randint(0, len(pidList))
    pidSelected = pidList[pidAleatory]

    pid = psutil.Process(pidSelected)

    try:
        pid = {
            'pid_id': pidSelected,
            'pid_name': pid.name(),
            'pid_exe': pid.exe(),
            'pid_date_creation': time.ctime(pid.create_time()),
            'pid_user_time': pid.cpu_times().user,
            'pid_system_time': pid.cpu_times().system,
            'pid_system_percent': pid.cpu_percent(interval=1.0),
            'pid_memory_percent': pid.memory_percent(),
            'pid_memory_use': pid.memory_info().rss,
            'pid_threads': pid.num_threads()

        }
    except Exception as error:
        print(f'Erro ao obter o PID: {str(error)}')
        pid = -1

    return pid
