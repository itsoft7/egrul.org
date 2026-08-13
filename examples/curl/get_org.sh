#!/bin/sh
# JSON и XML — для подписчиков (IP из личного кабинета или Bearer).

# JSON
curl -sL 'https://egrul.org/7730588444.json.gz' | gzip -dc

# XML
curl -sL 'https://egrul.org/7730588444.xml.gz' | gzip -dc

# с другого IP:
# curl -sL -H 'Authorization: Bearer email:token' \
#   'https://egrul.org/7730588444.xml.gz' | gzip -dc
