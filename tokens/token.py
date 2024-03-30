from abc import ABC, abstractmethod


class Token(ABC):
    @abstractmethod
    def draw(self, context) -> None:
        pass
