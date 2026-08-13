<?php
$json = gzdecode(file_get_contents('https://egrul.org/7730588444.json.gz'));
$data = json_decode($json, true);
echo json_encode($data, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
