''' loads pirate resources from net '''
import urllib.request


def loadHTML():
    # urllib.request.urlopen
    pass


def getPage (url):
    ''' download url and return string parsed as utf-8 '''

    with urllib.request.urlopen(url) as u:
        data = u.read().decode('utf-8')
    return data



def getAllPages():
    pass
