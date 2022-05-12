from functools import wraps
from typing import Callable

from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Dispatcher

from crawler.exceptions import InvalidArgumentError
from crawler.logs import get_logger

logger = get_logger(__name__)


def command_handler(command: str, *, dispatcher: Dispatcher) -> callable:

    """
    Decorates a function to handle the given command.
    """

    def _decorator(
        func: Callable[[str, Update, CallbackContext], str]
    ) -> Callable[[Update, CallbackContext], None]:
        @wraps(func)
        def _decorated(update: Update, context: CallbackContext) -> None:
            logger.info("Command %s was called!", command)

            message_text = update.message.text
            logger.info("Received message : %s", message_text)

            try:
                response = func(message_text, update=update, context=context)

            except InvalidArgumentError as exc:
                logger.error(exc, exc_info=True)

                response = str(exc)

            except Exception as exc:
                logger.error(exc, exc_info=True)

                response = (
                    "Oops! Something weird happened here, please try again later!"
                )

            logger.info("Command response : %s", response)

            update.message.reply_text(response)

        dispatcher.add_handler(CommandHandler(command, _decorated))

        return _decorated

    return _decorator
