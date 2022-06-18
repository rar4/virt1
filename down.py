import requests
import re
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-p', '--path', type=str, help='Path to page')
parser.add_argument('-n', '--number', type=int, help='number of links')
args = parser.parse_args()


def download_pages(p: str = 'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%'
                        'D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0',
                   number = 5):
    """takes link and number and installs pages from links on page< which link you inputed"""
    page = requests.get(p)
    b = page.text

    with open('pages/text.txt', 'a', encoding='utf-8') as f:
        f.write(b)

    with open('pages/text.txt', 'r', encoding='utf-8') as t:
        text = t.read()

    link = re.findall("(?P<url>https?://[^\s]+)", text)

    links = []

    for i in link:
        link.remove(i)
        for symbol in i:
            if symbol in [',', '"', "'", '<', '>', ']', '[']:
                i = i.replace(symbol, '')
        links.append(i)

    for num in range(number):
        with open(f"pages/{num}_page.txt", 'w', encoding='utf-8') as pg:
            ppg = requests.get(links[num])
            pg.write(ppg.text)
    print('finished')

download_pages(args.path, args.number)
