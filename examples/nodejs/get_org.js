#!/usr/bin/env node
const https = require('https');
const zlib = require('zlib');

function get(url, cb) {
  https.get(url, (res) => {
    const chunks = [];
    res.on('data', (c) => chunks.push(c));
    res.on('end', () => cb(zlib.gunzipSync(Buffer.concat(chunks)).toString('utf8')));
  }).on('error', console.error);
}

get('https://egrul.org/7730588444.json.gz', (json) => {
  console.log(JSON.stringify(JSON.parse(json), null, 2));
});
get('https://egrul.org/7730588444.xml.gz', (xml) => {
  console.log(xml);
});
