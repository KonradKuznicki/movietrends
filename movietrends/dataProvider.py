import downloader
import os

fromCache = False
dataFile = ''

def getData():
    if fromCache:
        downloader.getData()
    else:
        getDataFromFile(dataFile)

def getDataFromFile():
    os.

def cache():
    pass
