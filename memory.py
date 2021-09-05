import psutil


def getMemoryInfo():
    memory = psutil.virtual_memory()

    return memory
