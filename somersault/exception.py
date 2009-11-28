class UnknownToken(Exception):
    """
    Exception raised if the lexer encounters an unknown token.
    """
    def __init__(self, c):
        self.c = c

    def __str__(self):
        return "UknownToken:", c

class NoMoreTokens(Exception):
    """
    Exception raised if the lexer has no more tokens to parse.
    """
    pass
