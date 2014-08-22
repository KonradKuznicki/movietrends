import urllib.request, re

def getTrs(data):
    results = data.index('searchResult')
    start = data.index('/thead', results) + 7
    end = data.index('</table>', results)
    return data[start:end]


def getTitle(tr):
    return re.findall('detLink.*?>(.*?)</a>', tr)[0]

def filterWhiteSpace(name):
    return re.sub(r'[\W_]+', ' ', name).strip()

def getTitleAndYear(tr):
    name = getTitle(tr)
    m = re.findall('^(.*?)(19\d{2}|20\d{2})', name)
    if len(m) > 0:
        return [filterWhiteSpace(m[0][0]), m[0][1]]
    else:
        return [filterWhiteSpace(name), '']



def getFromPage(page):
    f = urllib.request.urlopen(page)
    data = f.read().decode('utf-8')
    trs = getTrs(data).split('</tr>\n	<tr>')
    return [getTitleAndYear(tr) for tr in trs]



def getTorrents(site, category):
    buf = []
    for i in range(100):
        buf += getFromPage(site + category + '/' + str(i) + '/3/')
    return buf


def transposeMatrix(matrix):
    return list(map(list, zip(*matrix)))
