from crawler.bot.decorators import command_handler
from crawler.bot.settings import TELEGRAM_BOT_TOKEN
from telegram import Update
from telegram.ext import CallbackContext, Updater

# Create the Updater and pass it your bot's token.
updater = Updater(TELEGRAM_BOT_TOKEN)
dispatcher = updater.dispatcher


@command_handler("start", dispatcher=dispatcher)
def start(message: str, **_kwargs) -> str:
    return "Vc enviou o comando start, parabéns seu imbecil!"


@command_handler("help", dispatcher=dispatcher)
def help(_message: str, **_kwargs) -> str:
    return "Oh agora vc mandou um help, quer um presente?"


@command_handler("dini", dispatcher=dispatcher)
def dini(_message: str, **_kwargs) -> str:
    return "Ah coisa mais gostosa desse mundo!!! S2"
