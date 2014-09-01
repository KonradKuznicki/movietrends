try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Shows movies good enought to pirate',
    'author': 'Konrad Kuznicki',
    'url': 'https://github.com/konradk2/movietrends',
    'download_url': 'https://github.com/konradk2/movietrends',
    'author_email': 'konrad@kuznicki.me',
    'version': '0.1',
    'install_requires': ['pytest', 'pyflakes'],
    'packages': ['movietrends'],
    'scripts': [],
    'name': 'movietrends'
}

setup(**config)
