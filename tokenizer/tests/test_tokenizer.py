import pytest

from tokenizer import Tokenizer, PythonTokenizer


class TestTokenizer:
    def test_tokenizer_creating_failed(self) -> None:
        with pytest.raises(TypeError):
            _ = Tokenizer()

    def test_python_tokenizer_creating(self) -> None:
        tokenizer = PythonTokenizer()
        assert isinstance(tokenizer, Tokenizer)
