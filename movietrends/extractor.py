import re


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
    m = re.findall(r'^(.*?)(19\d{2}|20\d{2})', name)

    if len(m) > 0:
        torrent = filterWhiteSpace(m[0][0])
        year = m[0][1]
    else:
        torrent = filterWhiteSpace(name)
        year = ''

    tds = re.findall(r'>(\d+)</', tr)
    if not len(tds):
        tds = [0, 0]
    seads, leaches = tds[len(tds)-2:]

    href = re.findall(r'href="(magnet.*?|/torrent.*?)"', tr)

    return [torrent, year, seads, leaches, href]


def parse_page(data):
    trs = getTrs(data).split('</tr>\n	<tr>')
    return [getTitleAndYear(tr) for tr in trs]
