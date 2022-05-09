from crawler.enums import ListTopThreadsPeriodEnum

PROGRAM_NAME = "Crawler"
PROGRAM_DESCRIPTION = """\
List the most highlighted threads in Reddit.\
"""

INPUT_UPVOTES_DEFAULT = 5000
INPUT_PERIOD_DEFAULT = ListTopThreadsPeriodEnum.PAST_24_HOURS.value

SOUP_FEATURES = "html.parser"
