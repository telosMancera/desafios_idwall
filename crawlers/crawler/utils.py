from crawler.logs import get_logger

logger = get_logger(__name__)


def prettify_object(
    obj: dict[str, any], *, header: str = "", item_mark: str = "*"
) -> str:

    """
    Prints an object in a prettier way.
    """

    prettier = ""

    if header:
        prettier += f"{header}\n\n"

    biggest_key_length = max(len(key) for key in obj)
    for key, value in obj.items():
        key = key.capitalize().replace("_", " ")
        prettier += f"{item_mark} {key:<{biggest_key_length}} : {value}\n"

    return "".join(prettier)
