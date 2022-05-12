from argparse import ArgumentParser as OriginalArgumentParser

from crawler.exceptions import InvalidArgumentError


class ArgumentParser(OriginalArgumentParser):

    """
    Customized ArgumentParser to improve error handling.
    """

    def error(self, message) -> None:
        if self.exit_on_error:
            super().error(message)

        else:
            raise InvalidArgumentError(f"{message}\n\n{self.format_usage()}")
