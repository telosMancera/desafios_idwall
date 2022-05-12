from enum import Enum


class _BaseEnum(Enum):

    """
    Adds some funcionalities to native Enum.
    """

    @classmethod
    def names(cls) -> tuple[str]:

        """
        List all names.
        """

        return tuple(item.name for item in cls)

    @classmethod
    def values(cls) -> tuple[any]:

        """
        List all values.
        """

        return tuple(item.value for item in cls)


class PeriodEnum(_BaseEnum):

    """
    Possible period values to be passed to crawler list_top_threads method.
    """

    LAST_HOUR = "hour"
    PAST_24_HOURS = "day"
    PAST_WEEK = "week"
    PAST_MONTH = "month"
    PAST_YEAR = "year"
    OF_ALL_TIME = "all"
