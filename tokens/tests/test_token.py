import pytest

from tokens import VariableToken, Token


class TestToken:
    def test_token_creating_failed(self) -> None:
        with pytest.raises(TypeError):
            _ = Token()

    def test_variable_token_creating(self) -> None:
        token = VariableToken('test')
        assert isinstance(token, Token)
