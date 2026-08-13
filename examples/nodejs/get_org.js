#!/usr/bin/env node
const https = require('https');
const zlib = require('zlib');

https.get('https://egrul.org/7730588444.json.gz', (res) => {
  const chunks = [];
  res.on('data', (c) => chunks.push(c));
  res.on('end', () => {
    const json = zlib.gunzipSync(Buffer.concat(chunks)).toString('utf8');
    console.log(JSON.stringify(JSON.parse(json), null, 2));
  });
}).on('error', console.error);
