class UnknownToken(Exception):
    """
    Exception raised if the lexer encounters an unknown token.
    """
    pass

class NoMoreTokens(Exception):
    """
    Exception raised if the lexer has no more tokens to parse.
    """
    pass
