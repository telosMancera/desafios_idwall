def print_pretty_object(
    obj: dict[str, any], *, header: str = "", item_mark: str = "*"
) -> None:

    """
    Prints an object in a prettier way.
    """

    if header:
        print(header)

    biggest_key_length = max(len(key) for key in obj)
    for key, value in obj.items():
        key = key.capitalize().replace("_", " ")
        print(f"  {item_mark} {key:<{biggest_key_length}} : {value}")
