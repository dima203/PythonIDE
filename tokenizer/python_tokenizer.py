from .tokenizer import Tokenizer

from tokens import FileToken, StringToken, VariableToken


class PythonTokenizer(Tokenizer):
    def tokenize(self, file) -> FileToken:
        result = FileToken()
        while line := file.readline():
            string = StringToken()
            string.add_child(VariableToken(line.rstrip()))
            result.add_child(string)
        return result
