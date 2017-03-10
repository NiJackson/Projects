'''Basic Web Scraper

first python web scrapper. following HTML Scraping
from The Hitchhiker's Guide to Python'''
#!\Python27\python
from sys import argv
from lxml import html
import requests


def harvest(url):
    '''Scraper function

    take url as command argument and pull page from url,
    returns tree structure'''
    page = requests.get(url)
    tree = html.fromstring(page.content)
    return tree

def xpath_parse(tree):
    '''XPath parsing function 
    
    '''
    test1 = tree.xpath('/html/body/p[2]/font/b/text()')
    test2 = tree.xpath('/html/body/p[46]/font/b/text()')
    print test1
    print test2
    return

def main():
    '''Main Function

    harvesting http://www.mit.edu/~xela/tao.html for first test'''
    xpath_parse(harvest(argv[1]))

if __name__ == '__main__':
    main()
