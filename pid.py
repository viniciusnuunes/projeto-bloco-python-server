import psutil
import random
import time


def getPid():
    pid_list = psutil.pids()
    pid_aleatory = random.randint(0, len(pid_list))
    pid_selected = pid_list[pid_aleatory]

    pid = psutil.Process(pid_selected)

    try:
        pid = {
            'pid_id': pid_selected,
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
