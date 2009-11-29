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

class NotImplemented(Exception):
    """
    Exception raised if the Node has not implemented an abstract method.
    """
    pass

class SyntaxError(Exception):
    """
    """
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        print msg
