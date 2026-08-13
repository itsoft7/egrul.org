#!/usr/bin/env python3
import gzip, json, urllib.request

def get(url):
    with urllib.request.urlopen(url) as response:
        return gzip.decompress(response.read())

data = json.loads(get('https://egrul.org/7730588444.json.gz'))
print(json.dumps(data, ensure_ascii=False, indent=2))

xml = get('https://egrul.org/7730588444.xml.gz').decode('utf-8')
print(xml)
