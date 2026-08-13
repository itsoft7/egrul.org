#!/bin/sh
# JSON — для подписчиков (IP из личного кабинета или Bearer).
curl -sL 'https://egrul.org/7730588444.json.gz' | gzip -dc

# с другого IP:
# curl -sL -H 'Authorization: Bearer email:token' \
#   'https://egrul.org/7730588444.json.gz' | gzip -dc
