# egrul.org

[API ЕГРЮЛ / ЕГРИП](https://egrul.org/) — выписки ФНС в XML и JSON, финансы, ФССП, проверки, справочники.

Это **публичный** репозиторий примеров и заметок. Исходный код сайта здесь не лежит.

Документация методов: [egrul.org](https://egrul.org/#Как_пользоваться).

## Быстрый старт

JSON и XML доступны [подписчикам](https://egrul.org/subscribe/): по IP из личного кабинета или заголовку

```
Authorization: Bearer email:token
```

Запрашивайте `.json.gz` или `.xml.gz` — сжатие уменьшает трафик примерно в 5 раз.

```php
<?php
// JSON
$json = gzdecode(file_get_contents('https://egrul.org/7730588444.json.gz'));
$data = json_decode($json, true);
echo json_encode($data, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);

// XML
$xml = gzdecode(file_get_contents('https://egrul.org/7730588444.xml.gz'));
echo $xml;
```

Примеры на других языках:

- [examples/php/get_org.php](examples/php/get_org.php)
- [examples/python/get_org.py](examples/python/get_org.py)
- [examples/nodejs/get_org.js](examples/nodejs/get_org.js)
- [examples/curl/get_org.sh](examples/curl/get_org.sh)
- [examples/mcp/](examples/mcp/) — вызов MCP-сервера (ChatGPT/Claude/др.) напрямую, без ИИ-клиента

Тот же блок — на [главной сайта](https://egrul.org/#Примеры_кода).

## Ответ

Корень JSON совпадает с XML ФНС (`СвЮЛ` / `СвИП`). Фрагменты: [JSON](examples/response.fragment.json), [XML](examples/response.fragment.xml). Описание формата:

- [организации](https://egrul.org/docs/16493030_1/16493030_1.html)
- [ИП](https://egrul.org/docs/16493030_2/16493030_2.html)

## Issues, PR, статьи

Ошибки в примерах и предложения — через Issues и Pull Request.

Статьи и разборы — в каталоге [`docs/`](docs/).
