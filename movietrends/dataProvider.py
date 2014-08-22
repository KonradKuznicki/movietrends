import downloader
import f
import json

fromCache = False
dataFile = ''

def getData():
    if fromCache:
        downloader.getData()
    else:
        getDataFromFile(dataFile)


def getDataFromFile():
    return json.loads(f.slurp(dataFile))


def putDataToFile():
    return f.spit(dataFile, json.dumps(downloader.getData()))


def cache():
    pass
