from .token import Token

from context import Context


class StringToken(Token):
    def __init__(self) -> None:
        super().__init__()
        self.__length: int = 0
        self.__tokens: list[Token] = []

    def draw(self, context: Context) -> None:
        pass

    def get_tree(self) -> dict:
        return {
            type(item).__name__: item.get_tree() for item in self.__tokens
        }

    def add_child(self, child: "Token") -> None:
        self.__tokens.append(child)
