from logging import INFO, Logger, basicConfig, getLogger

basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=INFO)


def get_logger(name: str) -> Logger:
    return getLogger(name)
