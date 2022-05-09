from enum import Enum


class ListTopThreadsPeriodEnum(Enum):

    """
    Possible period values to be passed to crawler list_top_threads method.
    """

    LAST_HOUR = "hour"
    PAST_24_HOURS = "day"
    PAST_WEEK = "week"
    PAST_MONTH = "month"
    PAST_YEAR = "year"
    OF_ALL_TIME = "all"
