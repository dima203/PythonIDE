from .token import Token


class VariableToken(Token):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.__name = name

    def draw(self, context) -> None:
        pass

    def get_tree(self) -> str:
        return self.__name
