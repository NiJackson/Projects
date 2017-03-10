'''Basic Web Scraper

first python web scrapper. following HTML Scraping
from The Hitchhiker's Guide to Python'''

from sys import argv
from lxml import html
import requests


def harvest(url):
    '''scraper function

    take url as command argument and pull page from url'''
    page = requesits.get(url)
    return

def main():
    '''Main Function

    '''
    harvest(argv[1])

if __name__ == '__main__':
    main()
