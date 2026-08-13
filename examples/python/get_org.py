#!/usr/bin/env python3
import gzip, json, urllib.request

url = 'https://egrul.org/7730588444.json.gz'
with urllib.request.urlopen(url) as response:
    data = json.loads(gzip.decompress(response.read()))
print(json.dumps(data, ensure_ascii=False, indent=2))
