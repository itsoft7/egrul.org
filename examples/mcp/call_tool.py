#!/usr/bin/env python3
"""
Пример вызова MCP-сервера egrul.org напрямую (без ИИ-клиента) — показывает
сам протокол JSON-RPC поверх HTTP, которым пользуются ChatGPT/Claude/другие
MCP-клиенты (подключение через них — https://egrul.org/#MCP_для_ИИ).

initialize и tools/list не требуют токена.
tools/call — нужен Authorization: Bearer email:token (тот же, что и для
остального API) либо OAuth (см. /.well-known/oauth-authorization-server).
"""
import json
import urllib.request

MCP_URL = 'https://egrul.org/mcp/'
EMAIL = 'you@example.com'
TOKEN = 'your_api_token'


def rpc(method, params=None, auth=False):
    body = json.dumps({
        'jsonrpc': '2.0',
        'id': 1,
        'method': method,
        'params': params or {},
    }).encode('utf-8')
    headers = {'Content-Type': 'application/json'}
    if auth:
        headers['Authorization'] = f'Bearer {EMAIL}:{TOKEN}'
    req = urllib.request.Request(MCP_URL, data=body, headers=headers)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


# Список инструментов — без токена.
tools = rpc('tools/list')
print('Доступные инструменты:', [t['name'] for t in tools['result']['tools']])

# Вызов инструмента — нужен токен подписки.
result = rpc('tools/call', {
    'name': 'org_lookup',
    'arguments': {'inn_or_ogrn': '7730588444'},
}, auth=True)
print(json.dumps(result, ensure_ascii=False, indent=2))
