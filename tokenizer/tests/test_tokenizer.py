import pytest

from tokenizer import Tokenizer, PythonTokenizer
from tokens import FileToken


class TestTokenizer:
    def test_tokenizer_creating_failed(self) -> None:
        with pytest.raises(TypeError):
            _ = Tokenizer()

    def test_python_tokenizer_creating(self) -> None:
        tokenizer = PythonTokenizer()
        assert isinstance(tokenizer, Tokenizer)

    def test_python_tokenizer_tokenize(self) -> None:
        with open('./tokenizer/tests/resources/file.py', 'r') as file:
            tokenizer = PythonTokenizer()
            result = tokenizer.tokenize(file)
            assert isinstance(result, FileToken)
            assert result.get_tree() == {
                1: {
                    'VariableToken': 'test'
                },
                2: {
                    'VariableToken': 'test2'
                }
            }
