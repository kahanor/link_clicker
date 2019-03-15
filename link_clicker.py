import json
import requests
import time
from bs4 import BeautifulSoup


def get_tor_session():
    session = requests.session()
    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session


def make_request(url):
    session = get_tor_session()
    print(session.get('http://httpbin.org/ip').text)
    response = session.get(url).content
    soup = BeautifulSoup(response, 'html.parser')
    print(soup.find('h4', {'class': 'alert-title'}))
    session.close()


with open('links.json') as links_file:
    urls = json.load(links_file)['urls']
    for i in range(7):
        for url in urls:
            make_request(url)
        time.sleep(24 * 60 * 60)
