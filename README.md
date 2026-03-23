# ZhuchkaKeyboards auth bot

Telegram-бот для экосистемы **ZhuchkaKeyboards**: тот же бот, что привязан к официальному **[Login Widget](https://core.telegram.org/widgets/login)** (домен и username бота в кнопке входа). Проверка подписи `hash` и выдача токенов выполняется в **`services/auth`** (OAuth); этот репозиторий — процесс **long polling** и обработчики в Telegram по шаблону ниже.

## Базовая архитектура

Проект основан на **[Reei-dp/aiogram-template](https://github.com/Reei-dp/aiogram-template)** (aiogram **3.21+**): структура `src/` (handlers, filters, keyboards, middlewares, FSM), конфигурация через INI, middleware для DI. Изменения в шаблоне лучше подтягивать осознанно (ветки, cherry-pick), не ломая свои хендлеры.

## Быстрый старт

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
copy config.ini.example config.ini
# Укажите token от @BotFather и при необходимости admin_ids
python -m src.main
```

Подробности по полям `config.ini` — в [upstream README](https://github.com/Reei-dp/aiogram-template#configuration) шаблона.

## Связанные документы

- Монорепозиторий: `docs/microservices/01-auth.md`, `docs/submodules.md` (путь `bots/auth_bot`).

## Лицензия

В корне лежит `LICENSE` из шаблона (MIT). Учёт авторства Reei-dp для исходного каркаса сохраняйте при существенном форке.
