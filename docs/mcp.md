# MCP-сервер egrul.org

[Model Context Protocol](https://modelcontextprotocol.io/) — открытый протокол,
по которому ИИ-агент (ChatGPT, Claude, Gemini, Perplexity, Grok и др.) сам
вызывает нужные инструменты стороннего сервера, без ручного копирования ссылок
и разбора JSON пользователем.

- URL сервера: `https://egrul.org/mcp/`
- Транспорт: Streamable HTTP (без SSE), JSON-RPC 2.0
- `initialize` и `tools/list` — без авторизации
- `tools/call` — нужна авторизация: OAuth 2.1 (PKCE + Dynamic Client
  Registration, автообнаружение по `/.well-known/oauth-authorization-server`)
  или заголовок `Authorization: Bearer email:token` напрямую (тот же токен,
  что и для остального API)
- Лимиты и биллинг — те же, что у остального API: запросы списываются с
  дневного лимита подписки

## Подключение в готовых клиентах

Инструкции для ChatGPT, Claude, Gemini, Perplexity и Grok —
[egrul.org/#MCP_для_ИИ](https://egrul.org/#MCP_для_ИИ). Коротко: добавить
коннектор по URL `https://egrul.org/mcp/`, тип авторизации — OAuth, дальше
вход тем же email и паролем, что в личном кабинете egrul.org.

## Вызов напрямую (без ИИ-клиента)

См. [`examples/mcp/`](../examples/mcp/) — минимальные примеры на Python и curl:
список инструментов через `tools/list` и вызов `org_lookup` через `tools/call`
с Bearer-токеном.

## Инструменты

Актуальный список и JSON-схемы параметров каждого инструмента — в ответе
`tools/list` самого сервера (он не дублируется здесь вручную, чтобы не
разъезжаться с реальным состоянием). На момент написания — карточка
организации/ИП, поиск по названию/email/региону, связи по ИНН, финансовая
отчётность, рейтинг компаний, санкции, иностранные агенты, Росфинмониторинг,
дисквалификация, розыск МВД/ФСИН, ежедневные списки новых/изменённых
организаций и ИП.

## Ещё способы использования API

- [Google Таблицы и Google Docs через Apps Script](https://egrul.org/articles/integraciya-ii-google-sheets-docs/)
