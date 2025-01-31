from pyformatter.settings import INPUT_JUSTIFY_DEFAULT, INPUT_LIMIT_DEFAULT
from pyformatter.utils import integer_division


class StringFormatter:
    def __init__(self, limit: int = INPUT_LIMIT_DEFAULT) -> None:
        self._limit = limit

    def format(self, text: str, *, justify: bool = INPUT_JUSTIFY_DEFAULT) -> str:

        """
        Formats the given text.
        """

        # Get original lines
        lines = self._get_lines(text)

        # Get the new lines according to limit
        new_lines = self._get_new_lines(lines)

        # Build the final string
        if not justify:
            return "\n".join(" ".join(line) for line in new_lines)

        # Justify the lines
        justified_lines = self._justify_lines(new_lines)

        return "\n".join(justified_lines)

    @staticmethod
    def _get_lines(text: str) -> list[list]:
        lines = []
        for line in text.split("\n"):
            words = line.split()
            if not words:
                lines.append("")

            else:
                lines.append(words)

        return lines

    def _get_new_lines(self, lines: list[list]) -> list[list]:
        new_lines = []
        for line in lines:
            if not line:
                new_lines.append("")

                continue

            new_line = []
            for word in line:
                if len(" ".join([*new_line, word])) <= self._limit:
                    new_line.append(word)

                    continue

                new_lines.append(new_line)
                new_line = [word]

            if new_line:
                new_lines.append(new_line)

        return new_lines

    def _justify_lines(self, new_lines: list[list]) -> list[str]:
        justified_lines = []
        for line in new_lines:
            if not line:
                justified_lines.append("")

                continue

            free_space = self._limit - sum(len(word) for word in line)
            if not free_space:
                justified_lines.append(" ".join(line))

                continue

            # Calculate the spaces' size
            number_of_spaces = (
                len(line) - 1  # 'one two tree' -> three words, two spaces
            )
            size_of_each_space, remaining_spaces = integer_division(
                free_space, number_of_spaces
            )

            # Create the spaces
            spaces = [" " * size_of_each_space] * number_of_spaces

            # Distribute the remaining spaces between the created spaces
            if remaining_spaces:
                for index, _ in enumerate(spaces):
                    spaces[index] += " "

                    remaining_spaces -= 1
                    if not remaining_spaces:
                        break

            # Create the justified line
            # The line is something like:
            #
            # > '{word1}{space1}{word2}{space2}..{wordN-1}{spaceN-1}{wordN}
            #
            word_space_pairs = zip(line[:-1], spaces)
            justified_line = (
                "".join(word + space for word, space in word_space_pairs) + line[-1]
            )

            justified_lines.append(justified_line)

        return justified_lines
