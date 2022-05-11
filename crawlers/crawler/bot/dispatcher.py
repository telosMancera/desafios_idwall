from crawler.bot.decorators import command_handler
from crawler.bot.settings import TELEGRAM_BOT_TOKEN
from crawler.exceptions import InvalidArgumentError
from crawler.functions import (
    list_top_threads,
    parse_execution_arguments,
    prettify_results,
)
from crawler.logs import get_logger
from telegram.ext import Updater

logger = get_logger(__name__)

updater = Updater(TELEGRAM_BOT_TOKEN)
dispatcher = updater.dispatcher


@command_handler("start", dispatcher=dispatcher)
def start(*_args, **_kwargs) -> str:
    return "Welcome to TelosIdCrawler!"


@command_handler("NadaPraFazer", dispatcher=dispatcher)
def nothing_to_do(message: str, **_kwargs) -> str:
    parsed_arguments = parse_execution_arguments(
        message.split()[1:], prog="/NadaPraFazer", exit_on_error=False
    )

    top_threads = list_top_threads(parsed_arguments)

    return prettify_results(top_threads, parsed_arguments)
