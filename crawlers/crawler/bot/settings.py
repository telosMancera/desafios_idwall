from os import environ

TELEGRAM_BOT_TOKEN = environ.get("TELEGRAM_BOT_TOKEN", None)
assert (
    TELEGRAM_BOT_TOKEN
), "The Telegram token must be set via TELEGRAM_BOT_TOKEN environment variable!"
