from .token import Token


class VariableToken(Token):
    def __init__(self, position: tuple[int, int]) -> None:
        super().__init__()
        self.position = position

    def draw(self, context) -> None:
        pass
