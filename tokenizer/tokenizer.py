from tokens import Token

from abc import ABC, abstractmethod


class Tokenizer(ABC):
    @abstractmethod
    def tokenize(self, file) -> Token:
        pass
