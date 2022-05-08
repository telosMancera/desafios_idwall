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
        lines = []
        for line in text.strip().split("\n"):
            words = line.split()
            lines.append(words)

        # Get the new lines according to limit
        new_lines = []
        for line in lines:
            new_line = []
            for word in line:
                if len(" ".join([*new_line, word])) <= self._limit:
                    new_line.append(word)

                    continue

                new_lines.append(new_line)
                new_line = [word]

            if new_line:
                new_lines.append(new_line)

        # Build the final string
        if not justify:
            return "\n".join(" ".join(line) for line in new_lines)

        # Justify the lines
        justified_lines = []
        for line in new_lines:
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

        return "\n".join(justified_lines)


if __name__ == "__main__":
    formatter = StringFormatter(40)
    # formatted = formatter.format(
    #     "In the beginning God     created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters."
    # )

    text = """
In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.

And God said, "Let there be light," and there was light. God saw that the light was good, and he separated the light from the darkness. God called the light "day," and the darkness he called "night." And there was evening, and there was morning - the first day.
    """

    print(formatter.format(text))
    print("")
    print(formatter.format(text, justify=True))
