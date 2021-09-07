import os


def getSimpleFiles():
    files = os.listdir()

    return files


def getDetailedFiles():
    files = os.listdir()

    dictFiles = {}

    for file in files:
        isFile = os.path.isfile(file)

        if isFile:
            print(file)
            dictFiles[file] = []

            dictFiles[file].append(os.stat(file).st_size)
            dictFiles[file].append(os.stat(file).st_atime)
            dictFiles[file].append(os.stat(file).st_mtime)

    return dictFiles


getSimpleFiles()
