from tokens import FileToken, StringToken, Token


class TestFileToken:
    def test_file_token_creating(self) -> None:
        token = FileToken()
        assert isinstance(token, FileToken)
        assert isinstance(token, Token)

    def test_file_token_tree(self) -> None:
        token = FileToken()
        assert token.get_tree() == {}

    def test_file_token_add_string(self) -> None:
        token = FileToken()
        assert token.get_tree() == {}
        token.add_child(StringToken())
        assert token.get_tree() == {1: {}}
