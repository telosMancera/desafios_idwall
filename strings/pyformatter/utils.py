def integer_division(a: int, b: int) -> tuple[int, int]:

    """
    Returns the quocient and remainder of the integer divsion between two numbers.
    """

    quocient = a // b
    remainder = a % b

    return quocient, remainder
