import json

with open('links.json') as links_file:
    urls = json.load(links_file)['urls']
