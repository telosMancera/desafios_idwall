from crawler.bot.dispatcher import updater
from crawler.logs import get_logger

logger = get_logger(__name__)


def main() -> None:
    # Run the bot until the user presses Ctrl-C
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
