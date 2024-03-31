from .token import Token
from .string_token import StringToken


class FileToken(Token):
    def __init__(self) -> None:
        super().__init__()
        self.__strings: list[StringToken] = []

    def draw(self, context) -> None:
        pass

    def get_tree(self) -> dict[int: dict]:
        return {
            i + 1: item.get_tree() for i, item in enumerate(self.__strings)
        }

    def add_child(self, child: StringToken) -> None:
        self.__strings.append(child)
