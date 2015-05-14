try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Zip file extractor',
    'author': 'Eric Kureck',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['extractor'],
    'scripts': [],
    'name': 'extractor'
}

setup(**config)
