#!/bin/sh
# MCP-сервер egrul.org — JSON-RPC поверх HTTP (Streamable HTTP, без SSE).
# Подключение через ChatGPT/Claude/другие MCP-клиенты — см. https://egrul.org/#MCP_для_ИИ

# tools/list — без токена
curl -s https://egrul.org/mcp/ \
  -X POST -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'

# tools/call — нужен Authorization: Bearer email:token (или OAuth)
curl -s https://egrul.org/mcp/ \
  -X POST -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer email:token' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"org_lookup","arguments":{"inn_or_ogrn":"7730588444"}}}'
