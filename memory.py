import psutil


def getMemoryInfo():
    memory = psutil.virtual_memory()

    memory = {
        'memory_total': memory[0],
        'memory_use': memory[3],
        'memory_free': memory[1],
        'memory_percent': memory[2],
        'memory_swap': psutil.swap_memory()
    }

    return memory
