from tokens import StringToken, VariableToken, Token


class TestStringToken:
    def test_string_token_creating(self) -> None:
        token = StringToken()
        assert isinstance(token, StringToken)
        assert isinstance(token, Token)

    def test_string_token_tree(self) -> None:
        token = StringToken()
        assert token.get_tree() == {}

    def test_string_token_add_string(self) -> None:
        token = StringToken()
        assert token.get_tree() == {}
        token.add_child(VariableToken('test'))
        assert token.get_tree() == {'VariableToken': 'test'}
