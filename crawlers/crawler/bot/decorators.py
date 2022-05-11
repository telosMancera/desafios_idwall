from functools import wraps
from typing import Callable

from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Dispatcher


def command_handler(command: str, *, dispatcher: Dispatcher) -> callable:

    """
    Decorates a function to handle the given command.
    """

    def _decorator(
        func: Callable[[str, Update, CallbackContext], str]
    ) -> Callable[[Update, CallbackContext], None]:
        @wraps(func)
        def _decorated(update: Update, context: CallbackContext) -> None:

            message_text = update.message.text

            response = func(message_text, update=update, context=context)

            update.message.reply_text(response)

        dispatcher.add_handler(CommandHandler(command, _decorated))

        return _decorated

    return _decorator
