''' loads pirate resources from net '''
import urllib.request


def getPage(url):
    ''' download url and return string parsed as utf-8 '''

    with urllib.request.urlopen(url) as u:
        data = u.read().decode('utf-8')
    return data


def getAllPages(url, start, end):
    return [getPage('{}/{}/3/'.format(url, i)) for i in range(start, end)]


url = 'http://pirateproxy.in/browse/207'
