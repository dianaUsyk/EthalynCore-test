# EthalynCore — State & Snapshots

Мета репозиторію — тримати **сталу робочу пам'ять** для проєкту Ethalyn:
- `cursor.yaml` — де ми зупинились і що далі (єдиний екземпляр, перезаписується);
- `mode.yaml` — активний робочий режим (єдиний екземпляр, перезаписується);
- `changelog/YYYY-MM.md` — історія змін, розбита помісячно (нові записи додаються в кінець файлу).

## Як працювати
1. Під час/після сесії створюємо *snapshot*.
2. Оновлюємо `cursor.yaml` і `mode.yaml`.
3. Додаємо пункт у відповідний `changelog/YYYY-MM.md`.
4. (Якщо налаштовано) n8n робить один коміт у GitHub.

## Структура
```
/cursor.yaml
/mode.yaml
/changelog/2025-08.md
/webhook/payload_example.json   # приклад корисного навантаження для n8n webhook
```

## Коміт-меседжі (рекомендація)
```
feat(memory): snapshot cursor + changelog entry
```
або
```
chore(snapshot): refresh cursor/mode
```

---

Останнє оновлення README: 2025-08-09T17:39:29+00:00
