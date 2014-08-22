import movietrends.downloader as downloader
import re

def test_basic():
    content = downloader.getPage('http://example.com/')
    assert(re.search('Example Domain', content))
