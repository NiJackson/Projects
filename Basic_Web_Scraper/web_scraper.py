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


def xpath_parser(tree, input_file):
    '''XPath parsing function

    read XPaths from txt file parse from tree and return list'''
    with open(input_file) as xpaths_file:
        return [tree.xpath(line) for line in xpaths_file]


def write_to_file(parsed_data, output_file):
    '''Write to File function

    take list of parsed xpath data from xpath_parser and
    wirte to output_file give as command argument'''
    with open(output_file, 'w') as output_file:
        for data in parsed_data:
            output_file.write(str(data))
            output_file.write('\n')
    return


def main():
    '''Main Function

    harvest page from url parse data from xpath in input file,
    write to output_file'''

    write_to_file(xpath_parser(harvest(argv[1]), argv[2]), argv[3])

if __name__ == '__main__':
    main()
