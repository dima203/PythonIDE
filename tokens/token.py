from abc import ABC, abstractmethod


from context import Context


class Token(ABC):
    @abstractmethod
    def draw(self, context: Context) -> None:
        pass

    @abstractmethod
    def get_tree(self) -> dict:
        pass

    def add_child(self, child: "Token") -> None:
        pass
