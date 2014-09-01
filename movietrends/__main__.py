import f
import downloader
import json
from extractor import parse_page
from itertools import chain


settings = {
    'cache_file': 'pages.json',
    'url': 'http://pirateproxy.in/browse/207',
    'start': 0,
    'end': 100
}


def spit_json(f_name, data):
    return f.spit(f_name, json.dumps(data))


def slurp_json(f_name):
    return json.loads(f.slurp(f_name))


def cache_requests(cache_file, url, start, end):
    spit_json(cache_file, downloader.getAllPages(url, start, end))


def cache_read(f_name):
    return slurp_json(f_name)


def parse_data():
    trends = list(chain(*map(parse_page,
                             cache_read(settings['cache_file']))))
    spit_json('parsed.json', trends)


def load_parsed():
    return cache_read('parsed.json')
